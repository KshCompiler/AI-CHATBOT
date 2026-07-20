from langchain.chat_models import init_chat_model

from chatbot.client import get_tools

llm = init_chat_model(
    model="openai/gpt-oss-120b",
    model_provider="groq",
)


async def get_llm_with_tools():
    tools = await get_tools()
    return llm.bind_tools(tools), tools
