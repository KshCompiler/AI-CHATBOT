from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import START, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition

from chatbot.llm import get_llm_with_tools
from chatbot.state import State


async def build_graph():
    llm_with_tools, tools = await get_llm_with_tools()

    def chatbot_node(state: State):
        return {"messages": [llm_with_tools.invoke(state.messages)]}

    graph_builder = StateGraph(State)

    graph_builder.add_node("chatbot", chatbot_node)
    graph_builder.add_node("tools", ToolNode(tools))

    graph_builder.add_edge(START, "chatbot")
    graph_builder.add_conditional_edges("chatbot", tools_condition)
    graph_builder.add_edge("tools", "chatbot")

    memory = InMemorySaver()
    return graph_builder.compile(checkpointer=memory)
