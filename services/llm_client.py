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
        **kwargs,
) -> ChatOpenAI:
    """构建一个 OpenAI 兼容的 ChatOpenAI 实例。"""
    return ChatOpenAI(
        model=model or LLM_MODEL,
        api_key=LLM_API_KEY,
        base_url=LLM_API_BASE,
        temperature=temperature if temperature is not None else LLM_TEMPERATURE,
        streaming=streaming,
        **kwargs,
    )


llm = get_llm(streaming=True)
