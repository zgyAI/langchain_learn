from langchain_core.tools import tool
from dotenv import load_dotenv
from pathlib import Path
from langchain_community.tools.tavily_search import TavilySearchResults
import os

Base_DIR = Path(__file__).resolve().parents[3]
env_path = Base_DIR / ".env"
load_dotenv(env_path)

tavily = TavilySearchResults(
    api_key=os.environ.get("TAVILY_API_KEY"),
    max_results=5)

# @tool("web_search", parse_docstring=True)
@tool
def web_search_old(query: str) -> str:
    """
    互联网搜索工具，可以搜索所有的信息
    Args:
        query: 需要进行互联网查询的信息
    Returns:
        返回搜索的结果信息，该信息
    """
    try:
        res = tavily.invoke(query)
        if not res:
            return "没有搜索结果"
        blocks = []
        for i, r in enumerate(res, 1):
            page_title = r.get('title',"")
            url = r.get('url',"")
            content = r.get('content',"") or r.get("snippet", "")
            blocks.append(f"{i}.{page_title}\n{url}\n{content}")
        return "\n\n".join(blocks)

    except Exception as e:
        print(e)
        return f"Error: {e}"

# if __name__ == "__main__":
    # print(web_search_old.name)
    # print(web_search_old.description)
    # print(web_search_old.invoke({'query': "机器学习"}))