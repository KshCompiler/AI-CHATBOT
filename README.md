# AI Chatbot

A conversational chatbot that remembers what you've told it and can search
the web on its own when a question needs current information it doesn't
already know.

## What it does

Talk to it like a normal chat assistant from your terminal. Within a
conversation, it keeps track of everything said so far, so you can refer
back to earlier messages without repeating yourself. When a question needs
up-to-date or outside knowledge — news, facts, anything past its training —
it decides on its own to run a web search and folds the results into its
answer, rather than guessing.

Conversation memory is in-process, so it resets when you stop the program.

## Running it

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

## Project structure

```
main.py            # entry point — runs the terminal chat loop
chatbot/
  state.py          # conversation state schema
  tools.py          # web search tool (Tavily)
  llm.py            # chat model setup, bound to tools
  graph.py          # builds the LangGraph chatbot graph
```
