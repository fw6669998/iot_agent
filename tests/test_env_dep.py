"""环境传递测试: 验证父进程环境能经由 claude code CLI 正确继承到其执行的子命令.

背景: services/ali_iot_tools.py 调用本地 claude code CLI 时, subprocess.run 未传 env=,
依赖父进程环境(含 PATH 决定的 python 解释器)被自动继承. 若该继承链断裂, claude 在设备
接入流程里生成并运行的 iot_connect.py 会跑在错误的 python 环境上(缺依赖 / 解释器不一致).

本文件以与生产代码相同的方式启动 claude, 让它运行一条 python 一行命令, 打印:
  1. 一个仅在父进程 os.environ 中注入的随机标记值 -- 验证 env 变量 父->claude->python 三级透传
  2. sys.executable 与 sys.version -- 即 claude 视角下的"当前 python 环境"

实测发现(见 test_claude_forwards_custom_env_var 的 xfail):
  * PATH 决定的 python 解释器/版本 能稳定透传 -- 设备接入所需的核心环境无误;
  * 但父进程的"自定义"环境变量经 Claude Code 的 bash 工具透传不稳定: 多数情况下能传到
    claude 的 python 子命令, 偶尔会被丢弃(原因在 Claude Code 内部, 非本进程 subprocess).
    因此不要依赖 os.environ 自动把自定义变量(如密钥/配置)带给 claude 生成的代码 --
    应在生成代码里显式写入/读取. 该用例以 xfail(strict=False) 跟踪此不稳定行为.
"""
import os
import shutil
import subprocess
import sys
import uuid

import pytest

# 与生产代码 (services/ali_iot_tools.py) 完全一致的 claude 启动参数
CLAUDE_CMD = ["claude", "-p", "--dangerously-skip-permissions", "--output-format", "text"]
# 仅注入 os.environ 用于探测传递链, 值为随机串, 不出现在 prompt 里, 故输出中出现即证明被读取
_MARKER_NAME = "IOT_AGENT_ENV_MARKER"


def _python_probe() -> str:
    """claude 需执行的 python 一行命令: 打印 标记值|解释器路径|版本号, 用 | 分隔便于解析.

    外层双引号、内层单引号, 在 bash 与 cmd 下均可原样传给 python -c. 标记为空时首字段为空串,
    仍能据 | 分辨出"命令确实执行了, 只是变量未透传".
    """
    return (
        "python -c \"import os,sys;"
        f"print(os.environ.get('{_MARKER_NAME}') or '', sys.executable, "
        "sys.version.split()[0], sep='|')\""
    )


def test_subprocess_inherits_env_without_env_arg(tmp_path, monkeypatch):
    """快速前置校验(不依赖 claude): 不传 env= 时, monkeypatch 注入 os.environ 的变量
    能被子进程读到. 证明 Python subprocess 的环境继承机制本身正常 -- 若 claude 链路里
    自定义 env 丢失, 原因在 Claude Code 的 bash 工具, 而非本进程的 subprocess 调用."""
    marker = f"MECH_{uuid.uuid4().hex}"
    monkeypatch.setenv(_MARKER_NAME, marker)

    proc = subprocess.run(
        [sys.executable, "-c",
         f"import os,sys;print(os.environ.get('{_MARKER_NAME}'),sys.executable)"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=30,
        cwd=tmp_path,
    )
    assert proc.returncode == 0, f"子进程异常: {proc.stderr}"
    out = proc.stdout.strip()
    assert marker in out, f"环境变量未被继承, 输出: {out!r}"
    assert sys.executable in out, f"解释器不一致, 输出: {out!r}"


@pytest.fixture(scope="module")
def claude_env_probe(tmp_path_factory):
    """运行一次 claude, 让它执行 python 探测命令并回显, 供多个断言复用, 避免重复慢启动.

    返回 {"marker": str, "output": str}. claude 缺失或超时则 skip 整个模块的相关测试.
    标记值只写入 os.environ(模块级 fixture 不能用 monkeypatch), 用完在 finally 清理.
    """
    if shutil.which("claude") is None:
        pytest.skip("未找到 claude 命令, 请确认已安装 Claude Code CLI 并加入 PATH")

    marker = f"CLAUDE_{uuid.uuid4().hex}"
    os.environ[_MARKER_NAME] = marker
    workdir = tmp_path_factory.mktemp("claude_ws")

    prompt = (
        "请用 bash 工具执行下面这条命令, 然后只把该命令的标准输出原样返回, "
        "不要添加任何解释、markdown 代码块或额外文字:\n\n"
        f"{_python_probe()}"
    )

    try:
        proc = subprocess.run(
            CLAUDE_CMD,
            input=prompt,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=600,
            cwd=workdir,
        )
    except subprocess.TimeoutExpired:
        pytest.skip("claude code cli 执行超时, 环境传递未能验证")
    finally:
        os.environ.pop(_MARKER_NAME, None)

    assert proc.returncode == 0, (
        f"claude 执行失败(returncode={proc.returncode}):\n"
        f"stdout={proc.stdout}\nstderr={proc.stderr}"
    )
    output = (proc.stdout or "").strip()
    print(f"[claude 原始输出]\n{output}")
    return {"marker": marker, "output": output}


def test_claude_sees_parent_python_environment(claude_env_probe):
    """主断言: claude 视角下的 python 解释器与版本应与本测试进程一致.

    PATH 被正确继承, 故 claude 运行 `python` 解析到的是同一解释器(含虚拟环境),
    设备接入流程里生成的 iot_connect.py 会跑在正确的 python 环境上.
    """
    out = claude_env_probe["output"]
    assert sys.executable in out, (
        f"claude 内 python 解释器与测试进程不一致: 期望 {sys.executable}, 输出: {out!r}"
    )
    version = ".".join(map(str, sys.version_info[:3]))
    assert version in out, (
        f"claude 内 python 版本与测试进程不一致: 期望 {version}, 输出: {out!r}"
    )


@pytest.mark.xfail(
    strict=False,
    reason=(
            "Claude Code 的 bash 工具对父进程自定义环境变量的透传不稳定(多数能传, 偶尔丢失, "
            "原因在其内部). strict=False 容许 xfail/xpass 两种结果均保持套件绿色, 并在报告中 "
            "显式呈现本次是否透传, 便于跟踪该行为是否趋于稳定."
    ),
)
def test_claude_forwards_custom_env_var(claude_env_probe):
    """自定义环境变量应能从父进程经 claude 透传到其 python 子命令.

    当前实测不稳定: 多数情况下标记值出现, 偶尔为空, 故 xfail(strict=False). 结论是
    不能可靠依赖 os.environ 自动把自定义变量带给 claude 生成的代码 -- 需在生成代码里
    显式写入/读取.
    """
    probe = claude_env_probe
    assert probe["marker"] in probe["output"], (
        f"环境变量 {_MARKER_NAME} 未透传到 claude 子进程, 输出: {probe['output']!r}"
    )


def testPythoneVersion():
    prompt = (
        "请执行该命令python --version, 然后只把该命令的标准输出原样返回, "
        "不要添加任何解释、markdown 代码块或额外文字:\n\n"
    )

    try:
        proc = subprocess.run(
            CLAUDE_CMD,
            input=prompt,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=600,
        )
    except subprocess.TimeoutExpired:
        pytest.skip("claude code cli 执行超时, 环境传递未能验证")
    finally:
        os.environ.pop(_MARKER_NAME, None)
    print('res:', proc.stdout, proc.stderr)
