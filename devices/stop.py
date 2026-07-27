"""
批量停止指定的 Python 进程
用法: python stop_processes.py              # 停止列表中所有进程
      python stop_processes.py iot.py       # 仅停止指定进程
      python stop_processes.py --list       # 查看哪些目标正在运行
"""

import sys
import time
import argparse
import psutil

# ============================================================
# 👇 在这里配置需要管理的 Python 程序列表
# ============================================================
TARGET_SCRIPTS = [
    # "iot_wechat.py",
    # "iot_computer.py"
    "iot_printter.py"
]
# ============================================================

GRACEFUL_TIMEOUT = 5  # SIGTERM 后等待优雅退出的秒数


def find_target_processes(targets: list[str]) -> dict[str, list[psutil.Process]]:
    """按脚本名分组查找匹配的进程"""
    result: dict[str, list[psutil.Process]] = {t: [] for t in targets}
    for proc in psutil.process_iter(["pid", "cmdline"]):
        try:
            cmdline = proc.info["cmdline"] or []
            for target in targets:
                if any(target == arg or arg.endswith("/" + target) or arg.endswith("\\" + target)
                       for arg in cmdline):
                    result[target].append(proc)
                    break
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return result


def stop_process(proc: psutil.Process, script_name: str) -> bool:
    """先 SIGTERM，超时后 SIGKILL，返回是否成功停止"""
    pid = proc.pid
    try:
        print(f"  ⏳ PID {pid:>6} | 发送 SIGTERM ...")
        proc.terminate()
        try:
            proc.wait(timeout=GRACEFUL_TIMEOUT)
            print(f"  ✅ PID {pid:>6} | 已优雅退出")
            return True
        except psutil.TimeoutExpired:
            print(f"  ⚠️  PID {pid:>6} | 超时未退出，发送 SIGKILL ...")
            proc.kill()
            proc.wait(timeout=3)
            print(f"  ✅ PID {pid:>6} | 已强制终止")
            return True
    except psutil.NoSuchProcess:
        print(f"  ℹ️  PID {pid:>6} | 进程已不存在")
        return True
    except psutil.AccessDenied:
        print(f"  ❌ PID {pid:>6} | 权限不足，无法终止")
        return False


def do_stop(targets: list[str]):
    grouped = find_target_processes(targets)
    total_stopped = 0
    total_failed = 0

    for script, procs in grouped.items():
        if not procs:
            print(f"\n🔍 {script}: 未找到运行中的进程")
            continue
        print(f"\n🛑 {script}: 找到 {len(procs)} 个进程")
        for proc in procs:
            if stop_process(proc, script):
                total_stopped += 1
            else:
                total_failed += 1

    print(f"\n{'=' * 40}")
    print(f"📊 完成: 成功停止 {total_stopped}, 失败 {total_failed}")


def do_list(targets: list[str]):
    grouped = find_target_processes(targets)
    print(f"{'脚本名':<25} {'PID':>8} {'状态':<10} {'命令行'}")
    print("-" * 80)
    found_any = False
    for script, procs in grouped.items():
        if not procs:
            print(f"{script:<25} {'—':>8} {'未运行':<10}")
        else:
            for proc in procs:
                try:
                    status = proc.status()
                    cmdline = " ".join(proc.cmdline() or [])[:50]
                    print(f"{script:<25} {proc.pid:>8} {status:<10} {cmdline}")
                    found_any = True
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass
    if not found_any:
        print("\n没有目标进程在运行")


def main():
    parser = argparse.ArgumentParser(description="批量停止指定的 Python 进程")
    parser.add_argument("scripts", nargs="*", help="要停止的脚本名（留空则停止全部）")
    parser.add_argument("--list", action="store_true", help="仅列出运行中的目标进程")
    args = parser.parse_args()

    targets = args.scripts if args.scripts else TARGET_SCRIPTS

    # 校验输入的脚本名是否在配置列表中
    unknown = set(targets) - set(TARGET_SCRIPTS)
    if unknown:
        print(f"⚠️  以下脚本不在配置列表中: {unknown}")
        print(f"   已配置的脚本: {TARGET_SCRIPTS}")
        sys.exit(1)

    if args.list:
        do_list(targets)
    else:
        do_stop(targets)


if __name__ == "__main__":
    main()
