# tools/web_tools.py
from langchain.tools import Tool
from serpapi import GoogleSearch
import os

# Your SerpAPI key
serpapi_key = os.getenv("SERPAPI_API_KEY")

def search_web(query):
    """Searches the web using SerpAPI."""
    params = {
        "q": query,
        "api_key": serpapi_key,
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    return results.get("organic_results", [])

web_search_tool = Tool(
    name="WebSearch",
    func=search_web,
    description="Performs web searches using SerpAPI."
)
