from langchain_core.tools import tool
from openai import api_key
from langchain_community.tools.tavily_search import TavilySearchResults
import os

tavily = TavilySearchResults(
    api_key=os.environ.get("TAVILY_API_KEY"),
    max_results=5)

# @tool("web_search", parse_docstring=True)
@tool
def web_search(query: str) -> str:
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

if __name__ == "__main__":
    print(web_search.name)
    print(web_search.description)
    print(web_search.invoke({'query': "机器学习"}))