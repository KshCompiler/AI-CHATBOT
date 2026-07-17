# AI Chatbot

A basic conversational chatbot built with LangGraph and Groq. It wraps a
single LLM call in a LangGraph graph, giving you a foundation to extend into
a multi-step or tool-using agent.

## Status

Early stage — currently a single Jupyter notebook (`basic chatbot/chatbot.ipynb`)
with a one-node graph that sends a message to the LLM and returns its reply.
`main.py` is an unrelated scaffold file from project init and isn't part of
the chatbot flow yet.

## Tech stack

- **[LangGraph](https://langchain-ai.github.io/langgraph/)** — orchestrates
  the chatbot as a graph (`StateGraph`) of nodes and edges.
- **[LangChain](https://python.langchain.com/)** — model-agnostic LLM
  interface (`init_chat_model`).
- **[Groq](https://groq.com/)** — LLM provider, using `llama-3.3-70b-versatile`.
- **LangSmith** — available for tracing/observability (via `langsmith` dependency).
- **Pydantic** — defines the graph's `state` schema.
- **[uv](https://docs.astral.sh/uv/)** — dependency and virtual environment manager.

## Prerequisites

- Python >= 3.14 (see `.python-version`)
- [uv](https://docs.astral.sh/uv/) installed
- A [Groq API key](https://console.groq.com/keys)

## Setup

```bash
# install dependencies into a local .venv
uv sync
```

Create a `.env` file in the project root (already git-ignored) with:

```
GROQ_API_KEY=your_groq_api_key_here
```

## Usage

Open `basic chatbot/chatbot.ipynb` and run the setup cell, which builds the
graph:

```python
llm = init_chat_model(model="llama-3.3-70b-versatile", model_provider="groq")

def chatbot(State: state):
    return {"messages": [llm.invoke(State.messages)]}

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)
graph = graph_builder.compile()
```

Then invoke it with a message:

```python
response = graph.invoke({"messages": [{"role": "user", "content": "hello"}]})
print(response["messages"][-1].content)
```

## Project structure

```
.
├── basic chatbot/
│   └── chatbot.ipynb    # the chatbot graph: state, node, edges, and a test run
├── main.py              # unused scaffold entry point from project init
├── pyproject.toml       # project metadata and dependencies (uv-managed)
├── requirements.txt     # plain pip-installable dependency list
├── uv.lock              # locked dependency versions
└── .env                 # GROQ_API_KEY (not committed)
```
