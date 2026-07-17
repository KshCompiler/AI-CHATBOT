# AI Chatbot

A conversational chatbot that remembers what you've told it and can search
the web on its own when a question needs current information it doesn't
already know.

## What it does

Talk to it like a normal chat assistant. Within a conversation, it keeps
track of everything said so far, so you can refer back to earlier messages
without repeating yourself. When a question needs up-to-date or
outside knowledge — news, facts, anything past its training — it decides on
its own to run a web search and folds the results into its answer, rather
than guessing.

It's currently built and run from a single notebook
(`basic chatbot/chatbot.ipynb`), not a packaged app — the memory is
in-process, so conversation history resets when the notebook's kernel is
restarted.

## Running it

```bash
uv sync
```

Add your API keys to a `.env` file in the project root:

```
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

Then open `basic chatbot/chatbot.ipynb`, run the first cell to build the
chatbot, and talk to it by invoking the graph with a `thread_id` (this is
what lets it remember the conversation):

```python
config = {"configurable": {"thread_id": "1"}}
response = graph.invoke({"messages": [{"role": "user", "content": "hello"}]}, config)
print(response["messages"][-1].content)
```

Keep reusing the same `thread_id` to continue the same conversation; use a
new one to start a fresh, unrelated chat.
