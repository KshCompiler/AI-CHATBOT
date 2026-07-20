from mcp.server.fastmcp import FastMCP
from langchain_tavily import TavilySearch
from dotenv import load_dotenv

load_dotenv()

mcp = FastMCP("servers")

@mcp.tool()
def searchEngine(query:str)->str:
    """ search web whenever necessary"""
    search = TavilySearch(max_results=2, include_answer="True")

    result = search.invoke(query)
    
    return result["answer"]
    
searchEngine("todays news")
if __name__ == "__main__":
    mcp.run()
