# agents/search_agent.py
from langchain.agents import initialize_agent, Tool
from langchain_openai import ChatOpenAI
from tools.web_tools import web_search_tool
from mcp.context_manager import ContextManager
from mcp.message import MCPMessage
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Define SearchAgent
def run_search_agent(context: ContextManager):
    """Runs the SearchAgent and sends search results to ReaderAgent."""
    # Get any pending messages for the SearchAgent
    messages = context.get_messages_for("search_agent")
    
    for msg in messages:
        query = msg.payload["query"]  # Query to search
        
        # Use LangChain's agent to perform search
        print("🔑 OPENAI_API_KEY =", os.getenv("OPENAI_API_KEY"))

        llm = ChatOpenAI()
        tools = [web_search_tool]
        agent = initialize_agent(tools, llm, agent_type="zero-shot-react-description")
        
        try:
            # Run the search task
            search_results = agent.run(f"Search for: {query}")
            
            # Clean up the output if needed (in case there are action-based responses)
            cleaned_results = search_results.split("Action:")[0].strip()  # Taking only the relevant part
            
            # Process and forward results to ReaderAgent
            new_msg = MCPMessage(
                sender="search_agent",
                receiver="reader_agent",
                task_type="summarize_results",
                payload={
                    "search_results": cleaned_results,
                    "topic": msg.payload.get("topic", "AI")  # Default fallback just in case
                }
            )

            context.send_message(new_msg)

        except Exception as e:
            print(f"❌ Error running search task: {str(e)}")
            # Handle error gracefully, maybe send a message back with an error status
            error_msg = MCPMessage(
                sender="search_agent",
                receiver="reader_agent",
                task_type="error",
                payload={"error_message": str(e)}
            )
            context.send_message(error_msg)
