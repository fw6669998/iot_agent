"""LLM 流式调用诊断测试.

背景: connectDeviceToPlatformCode 中 llm_client.llm.stream() 收到的 chunk 流,
content 恒为空, 无法提取生成文本. 本测试用最小 prompt 复现, 打印 chunk 结构与字段
分布, 定位文本所在字段(content / reasoning_content / 其它), 并断言能提取到非空文本.
"""
import time

import pytest

from langchain_core.messages import HumanMessage

from services import llm_client


def test_llm_stream_yields_content():
    """流式调用应能提取到非空文本, 兼容 content 与 reasoning_content 两种落点."""
    messages = [HumanMessage(content="请只回复两个字:你好")]

    chunks = []
    reasoning_chunks = []
    total = 0
    content_nonempty = 0
    samples = []

    # request_timeout=60 避免测试长时间挂起; streaming=True 复现生产流式行为
    for chunk in llm_client.get_llm(streaming=True, request_timeout=60).stream(messages):
        total += 1
        text = chunk.content if isinstance(chunk.content, str) else ""
        reasoning = ""
        if chunk.additional_kwargs:
            reasoning = (chunk.additional_kwargs.get("reasoning_content")
                         or chunk.additional_kwargs.get("reasoning") or "")
        if text:
            content_nonempty += 1
            chunks.append(text)
        if reasoning:
            reasoning_chunks.append(reasoning)
        # 采样: 前5个 + 每10个1个, 覆盖全程结构
        if total <= 5 or total % 10 == 0:
            samples.append(f"#{total}: {repr(chunk)[:400]}")

    result_text = "".join(chunks) or "".join(reasoning_chunks)

    print(f"\n[diag] 共 {total} 个chunk, content非空 {content_nonempty} 个")
    print(f"[diag] 提取结果({len(result_text)}字符): {result_text[:300]!r}")
    print("[diag] chunk样本:")
    for s in samples:
        print(f"  {s}")

    assert result_text, f"未提取到任何文本: 共{total}个chunk, content非空{content_nonempty}"


def test_llm_stream_generates_code():
    """贴近真实场景: 让模型生成一段代码, 验证 content 能正常流式输出(非空且较长).

    connectDeviceToPlatformCode 的实际 prompt 让模型生成完整接入代码, 本用例以更小的
    代码生成任务复现同一路径, 确认 content 字段在生成场景下同样可提取.
    """
    messages = [HumanMessage(content="用python写一个add函数,只返回代码,不要解释")]

    chunks = []
    total = 0
    content_nonempty = 0
    for chunk in llm_client.get_llm(streaming=True, request_timeout=60).stream(messages):
        total += 1
        text = chunk.content if isinstance(chunk.content, str) else ""
        if text:
            content_nonempty += 1
            chunks.append(text)

    result_text = "".join(chunks)
    print(f"\n[diag] 生成代码: 共{total}个chunk, content非空{content_nonempty}个, 结果{len(result_text)}字符")
    print(f"[diag] 结果前200字符: {result_text[:200]!r}")

    assert result_text, f"未提取到代码: 共{total}个chunk, content非空{content_nonempty}"
    assert "def" in result_text or "add" in result_text, f"结果不像代码: {result_text!r}"


def test_llm_stream_real_prompt():
    """用接近真实的复杂 prompt(模板代码 + tsl.json)复现 connectDeviceToPlatformCode 调用.

    短 prompt 不触发深度推理, 本用例以真实长 prompt 验证复杂任务下 content 是否仍能正常
    流式输出, 并记录 reasoning tokens 与耗时, 排查"content 长时间为空"的根因.
    """
    import json
    import os

    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(root, "doc", "template_iot_connect.py"), encoding="utf-8") as f:
        code = f.read()
    with open(os.path.join(root, "devices", "computer", "tsl.json"), encoding="utf-8") as f:
        model_text = json.dumps(json.load(f), ensure_ascii=False, indent=2)

    task_prompt = (
        "你是物联网设备接入专家。请根据用户需求生成代码\n"
        "一般是让你帮忙将设备接入阿里云物联网平台, 也有可能让你帮忙解决bug\n"
        "设备接入要求:\n"
        "- 依据物模型 properties 实现属性上报, 依据 services 实现服务调用处理与回复\n"
        "- 属性10s一检测,变化才上报且只上报变化的属性\n"
        "- 接入成功后让接入程序在后台运行,但不要设置开机运行\n"
        "- 接入程序加上日志,每条日志有时间\n"
        "- 使用python语言编写代码,代码尽量简洁\n"
        f"【用户需求】\n帮我把我这台电脑接入阿里云物联网平台\n\n"
        f"【tsl.json】\n{model_text}\n\n"
        f"【模版代码】\n{code}\n\n"
    )

    messages = [HumanMessage(content=task_prompt)]
    chunks = []
    total = 0
    content_nonempty = 0
    reasoning_tokens = None
    t0 = time.time()
    for chunk in llm_client.get_llm(streaming=True, request_timeout=180).stream(messages):
        total += 1
        text = chunk.content if isinstance(chunk.content, str) else ""
        if text:
            content_nonempty += 1
            chunks.append(text)
        if chunk.usage_metadata and chunk.usage_metadata.get("output_token_details"):
            reasoning_tokens = chunk.usage_metadata["output_token_details"].get("reasoning")
    elapsed = time.time() - t0
    result_text = "".join(chunks)

    print(f"\n[diag] 真实prompt {len(task_prompt)}字符: 共{total}个chunk, content非空{content_nonempty}个, "
          f"耗时{elapsed:.1f}s, reasoning_tokens={reasoning_tokens}")
    print(f"[diag] 结果{len(result_text)}字符, 前300: {result_text[:300]!r}")

    assert result_text, (
        f"真实prompt未提取到文本! 共{total}个chunk, content非空{content_nonempty}, "
        f"reasoning_tokens={reasoning_tokens}, 耗时{elapsed:.1f}s"
    )


def test_qwen_disable_thinking_real_prompt():
    """用 openai 原生客户端验证 qwen3.8-max 的思考行为与关闭方式.

    根因排查: langchain 未解析 DashScope 的 reasoning_content, 导致思考阶段 content 全空.
    本用例绕开 langchain, 直接读取 delta.content 与 delta.reasoning_content, 确认:
      1) 关闭思考(enable_thinking=False)后 content 是否直接输出;
      2) reasoning_content 字段是否真实存在(证明 langchain 丢失了它).
    """
    import json
    import os
    from openai import OpenAI

    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(os.path.join(root, "doc", "template_iot_connect.py"), encoding="utf-8") as f:
        code = f.read()
    with open(os.path.join(root, "devices", "computer", "tsl.json"), encoding="utf-8") as f:
        model_text = json.dumps(json.load(f), ensure_ascii=False, indent=2)
    task_prompt = (
        "你是物联网设备接入专家。请根据用户需求生成代码\n"
        "设备接入要求:\n"
        "- 依据物模型 properties 实现属性上报, 依据 services 实现服务调用处理与回复\n"
        "- 属性10s一检测,变化才上报且只上报变化的属性\n"
        "- 使用python语言编写代码,代码尽量简洁\n"
        f"【用户需求】\n帮我把我这台电脑接入阿里云物联网平台\n\n"
        f"【tsl.json】\n{model_text}\n\n"
        f"【模版代码】\n{code}\n\n"
    )

    client = OpenAI(api_key=os.getenv("LLM_API_KEY"), base_url=os.getenv("LLM_API_BASE"))
    stream = client.chat.completions.create(
        model=os.getenv("LLM_MODEL"),
        messages=[{"role": "user", "content": task_prompt}],
        stream=True,
        extra_body={"enable_thinking": False},
        stream_options={"include_usage": True},
    )
    content_parts = []
    reasoning_parts = []
    for chunk in stream:
        if chunk.choices:
            delta = chunk.choices[0].delta
            if delta.content:
                content_parts.append(delta.content)
            rc = getattr(delta, "reasoning_content", None)
            if rc:
                reasoning_parts.append(rc)
    content_text = "".join(content_parts)
    reasoning_text = "".join(reasoning_parts)

    print(f"\n[diag] enable_thinking=False: content={len(content_text)}字符, "
          f"reasoning={len(reasoning_text)}字符")
    print(f"[diag] content前300: {content_text[:300]!r}")
    print(f"[diag] reasoning前200: {reasoning_text[:200]!r}")

    assert content_text, (
        f"关闭思考后 content 仍为空! reasoning={len(reasoning_text)}字符 -- "
        "qwen3.8-max 可能是仅思考模式(无法关闭), 需改为解析 reasoning_content 或换非思考模型"
    )
