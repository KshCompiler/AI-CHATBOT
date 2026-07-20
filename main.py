from dotenv import load_dotenv

from chatbot import build_graph

load_dotenv()


def main():
    graph = build_graph()
    config = {"configurable": {"thread_id": "1"}}

    print("Chatbot ready. Type 'exit' to quit.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("exit", "quit"):
            break

        response = graph.invoke({"messages": [{"role": "user", "content": user_input}]}, config)
        print(f"Bot: {response['messages'][-1].content}")


if __name__ == "__main__":
    main()
