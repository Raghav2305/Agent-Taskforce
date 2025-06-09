import random
from mcp.context_manager import ContextManager
from mcp.message import MCPMessage
from agents import search_agent, reader_agent, writer_agent
from tools.email_sender import send_email
from config.predefined_queries import predefined_queries

def main():
    context = ContextManager()

    item = random.choice(predefined_queries)
    print(f"\n📩 Processing Query: {item['query']}")

    # Step 1: Send to search agent
    msg = MCPMessage(
        sender="user",
        receiver="search_agent",
        task_type="search_task",
        payload={
            "query": item["query"],
            "topic": item["topic"]  # pass topic to reader for prompt use
        }
    )
    context.send_message(msg)

    print("🔍 Running Search Agent")
    search_agent.run_search_agent(context)

    print("📖 Running Reader Agent")
    reader_agent.run_reader_agent(context)

    print("✍️ Running Writer Agent")
    writer_agent.run_writer_agent(context)

    # Send the email for each query
    if hasattr(context, "latest_email"):
        send_email(
            to_email="raghavkavimandan23@gmail.com",
            subject=context.latest_email["subject"],
            body_html=context.latest_email["body"]
        )
    else:
        print("📭 No email content available to send.")

if __name__ == "__main__":
    main()
