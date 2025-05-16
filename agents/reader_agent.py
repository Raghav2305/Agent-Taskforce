# reader_agent.py

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from mcp.message import MCPMessage

def run_reader_agent(context):
    messages = context.get_messages_for("reader_agent")
    if not messages:
        return

    message = messages[0]
    query_results = message.payload.get("search_results", [])

    # Combine all search results into a single string for summarization
    combined_text = "\n\n".join(query_results)

    # Set up LLM summarization
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.3)

    prompt = PromptTemplate.from_template(
    "Based on the following search results, write a detailed article suitable for an AI research newsletter focusing on {topic}:\n\n{results}\n\nFormat it professionally with clear, informative language."
)

    topic = message.payload.get("topic", "AI")

    chain = LLMChain(llm=llm, prompt=prompt)
    summary = chain.run({"results": combined_text, "topic": topic})
    # chain = LLMChain(llm=llm, prompt=prompt)
    # summary = chain.run({"results": combined_text})

    # Send to writer agent with proper key
    response = MCPMessage(
    sender="reader_agent",
    receiver="writer_agent",
    task_type="generate_output",
    payload={
        "summarized_results": summary,
        "topic": topic
    }
    )

    context.send_message(response)
