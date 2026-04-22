from rag.rag_pipeline import create_vectorstore
from agent.agent_graph import AgentState, run_agent


def main():
    print("AutoStream AI Agent is running...\n")

    # Create RAG system
    vectorstore = create_vectorstore()

    # Initialize state (memory)
    state = AgentState()

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        response = run_agent(user_input, state, vectorstore)
        print("Agent:", response)


if __name__ == "__main__":
    main()
