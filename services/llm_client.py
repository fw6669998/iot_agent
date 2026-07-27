import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

LLM_MODEL = os.getenv("LLM_MODEL")
LLM_API_BASE = os.getenv("LLM_API_BASE")
LLM_API_KEY = os.getenv("LLM_API_KEY")
LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", "0.7"))


def get_llm(
        model: str | None = None,
        temperature: float | None = None,
        streaming: bool = False,
        enable_thinking: bool = True,
        **kwargs,
) -> ChatOpenAI:
    """构建一个 OpenAI 兼容的 ChatOpenAI 实例。

    enable_thinking 默认 False: qwen3 系列默认开启思考模式, 思考内容走 reasoning_content
    字段而非 content, 流式时 content 长时间为空(且 langchain 未解析 reasoning_content),
    表现为"无响应". 关闭后模型直接输出 content, 适合代码生成等无需展示思考过程的场景.
    需要思考时传 enable_thinking=True.
    """
    return ChatOpenAI(
        model=model or LLM_MODEL,
        api_key=LLM_API_KEY,
        base_url=LLM_API_BASE,
        temperature=temperature if temperature is not None else LLM_TEMPERATURE,
        streaming=streaming,
        extra_body={"enable_thinking": enable_thinking},
        **kwargs,
    )


llm = get_llm(streaming=True)
