import asyncio
import sys

from dotenv import load_dotenv

load_dotenv()

sys.stdout.reconfigure(encoding="utf-8")

from chatbot import build_graph


async def main():
    graph = await build_graph()
    config = {"configurable": {"thread_id": "1"}}

    print("Chatbot ready. Type 'exit' to quit.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("exit", "quit"):
            break

        response = await graph.ainvoke({"messages": [{"role": "user", "content": user_input}]}, config)
        print(f"Bot: {response['messages'][-1].content}")


if __name__ == "__main__":
    asyncio.run(main())
