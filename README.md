# AI Chatbot

A tool-using conversational chatbot built with LangGraph and Groq. The
model can search the web via Tavily when it needs current information, and
conversations are kept in memory across turns within a session.

## Status

Currently a single Jupyter notebook (`basic chatbot/chatbot.ipynb`) holding
the working graph, plus a couple of exploratory cells. `main.py` is an
unrelated scaffold file from project init and isn't part of the chatbot
flow.

## Tech stack

- **[LangGraph](https://langchain-ai.github.io/langgraph/)** — orchestrates
  the chatbot as a graph (`StateGraph`) of nodes and edges, including a
  conditional tool-calling loop.
- **[LangChain](https://python.langchain.com/)** — model-agnostic LLM
  interface (`init_chat_model`) and tool-binding (`bind_tools`).
- **[Groq](https://groq.com/)** — LLM provider, using `llama-3.3-70b-versatile`.
- **[Tavily](https://tavily.com/)** — web search tool (`langchain-tavily`)
  the model can call for up-to-date information.
- **LangSmith** — available for tracing/observability (via `langsmith` dependency).
- **Pydantic** — defines the graph's `state` schema.
- **[uv](https://docs.astral.sh/uv/)** — dependency and virtual environment manager.

## Prerequisites

- Python >= 3.14 (see `.python-version`)
- [uv](https://docs.astral.sh/uv/) installed
- A [Groq API key](https://console.groq.com/keys)
- A [Tavily API key](https://app.tavily.com/)

## Setup

```bash
# install dependencies into a local .venv
uv sync
```

Create a `.env` file in the project root (already git-ignored) with:

```
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

## Usage

Open `basic chatbot/chatbot.ipynb` and run the first cell, which builds the
graph:

```python
llm = init_chat_model(model="llama-3.3-70b-versatile", model_provider="groq")

tavily_tool = TavilySearch(max_results=2)
tools = [tavily_tool]
llm_with_tools = llm.bind_tools(tools)

def chatbot(State: state):
    return {"messages": [llm_with_tools.invoke(State.messages)]}

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("tools", ToolNode(tools))

graph_builder.add_edge(START, "chatbot")
graph_builder.add_conditional_edges("chatbot", tools_condition)
graph_builder.add_edge("tools", "chatbot")

memory = InMemorySaver()
graph = graph_builder.compile(checkpointer=memory)
```

The graph flow: `START → chatbot`, then `tools_condition` checks whether the
model asked to call a tool — if so it routes to `tools` (runs the Tavily
search and feeds results back into `chatbot`), otherwise it routes to `END`.

Invoke it with a `thread_id` so the conversation is remembered across calls:

```python
config = {"configurable": {"thread_id": "1"}}
response = graph.invoke({"messages": [{"role": "user", "content": "hello"}]}, config)
print(response["messages"][-1].content)
```

Memory is powered by `InMemorySaver`, which is in-process only — history
resets whenever the kernel restarts.

You can also visualize the compiled graph inline:

```python
from IPython.display import Image, display
display(Image(graph.get_graph().draw_mermaid_png()))
```

## Project structure

```
.
├── basic chatbot/
│   └── chatbot.ipynb    # the chatbot graph: state, tool-bound model, nodes, edges, memory
├── main.py              # unused scaffold entry point from project init
├── pyproject.toml       # project metadata and dependencies (uv-managed)
├── requirements.txt     # plain pip-installable dependency list
├── uv.lock              # locked dependency versions
└── .env                 # GROQ_API_KEY and TAVILY_API_KEY (not committed)
```
