# AI Chatbot

A conversational chatbot that remembers what you've told it, can search the
web on its own when a question needs current information it doesn't already
know, and can read, write, and browse files in this project's directory when
asked to.

## What it does

Talk to it like a normal chat assistant from your terminal. Within a
conversation, it keeps track of everything said so far, so you can refer
back to earlier messages without repeating yourself. When a question needs
up-to-date or outside knowledge — news, facts, anything past its training —
it decides on its own to run a web search and folds the results into its
answer, rather than guessing. It can also list, read, write, move, and search
files within this project's folder when asked to work with local files.

Conversation memory is in-process, so it resets when you stop the program.

## Running it

Requires [uv](https://docs.astral.sh/uv/) for Python dependencies and
Node.js (for `npx`) to run the filesystem tool server.

```bash
uv sync
```

Add your API keys to a `.env` file in the project root:

```
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

Then start the chatbot:

```bash
uv run main.py
```

Type your messages at the `You:` prompt; type `exit` or `quit` to end the
session.

## Tools

The chatbot's tools run behind the Model Context Protocol (MCP) — the chat
model talks to local MCP servers rather than calling any APIs directly:

- **Web search** — a local MCP server wraps Tavily search.
- **Filesystem access** — the official `@modelcontextprotocol/server-filesystem`
  MCP server (run via `npx`), scoped to this project's directory only. The
  model can list, read, write, move, and search files within the project,
  but nothing outside it.

  To allow a different directory, change `PROJECT_ROOT` in
  `chatbot/client.py`:

  ```python
  PROJECT_ROOT = Path(__file__).parent.parent  # default: this project's folder

  # example: allow a specific folder instead
  PROJECT_ROOT = Path(r"C:\Users\kshit\OneDrive\Desktop\some-other-folder")
  ```

## Project structure

```
main.py            # entry point — runs the terminal chat loop
chatbot/
  state.py          # conversation state schema
  servers.py        # MCP server exposing the Tavily web search tool
  client.py         # MCP client — connects to servers.py and the filesystem MCP server, loads their tools
  llm.py            # chat model setup, bound to the MCP-provided tools
  graph.py          # builds the LangGraph chatbot graph
```
