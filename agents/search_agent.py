# agents/search_agent.py
from langchain.agents import initialize_agent, Tool
from langchain_openai import ChatOpenAI
from tools.web_tools import web_search_tool
from mcp.context_manager import ContextManager
from mcp.message import MCPMessage
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def run_search_agent(context: ContextManager):
    messages = context.get_messages_for("search_agent")
    
    for msg in messages:
        query = msg.payload["query"]
        
        llm = ChatOpenAI()
        tools = [web_search_tool]

        agent = initialize_agent(
            tools,
            llm,
            agent_type="zero-shot-react-description",
            handle_parsing_errors=True,  # This helps with output parsing retries
        )
        
        try:
            # Use invoke instead of deprecated run
            response = agent.invoke({"input": f"Search for: {query}"})
            search_results = response.get("output", "")

            # If you want to be safe, remove any trailing agent "Action:" or internal text manually but carefully
            # Example (optional):
            if "Action:" in search_results:
                search_results = search_results.split("Action:")[0].strip()

            # Send results to reader agent
            new_msg = MCPMessage(
                sender="search_agent",
                receiver="reader_agent",
                task_type="summarize_results",
                payload={
                    "search_results": search_results,
                    "topic": msg.payload.get("topic", "AI")
                }
            )
            context.send_message(new_msg)

        except Exception as e:
            print(f"❌ Error running search task: {str(e)}")
            error_msg = MCPMessage(
                sender="search_agent",
                receiver="reader_agent",
                task_type="error",
                payload={"error_message": str(e)}
            )
            context.send_message(error_msg)
