from langchain.chat_models import init_chat_model

from chatbot.tools import tools

llm = init_chat_model(
    model="llama-3.3-70b-versatile",
    model_provider="groq",
)

llm_with_tools = llm.bind_tools(tools)
