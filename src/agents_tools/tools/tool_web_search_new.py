from langchain_core.tools import tool
from dotenv import load_dotenv
from pathlib import Path
from langchain_tavily import TavilySearch
import os

Base_DIR = Path(__file__).resolve().parents[3]
env_path = Base_DIR / ".env"
load_dotenv(env_path)

tavily = TavilySearch(
    api_key=os.environ.get("TAVILY_API_KEY"),
    max_results=5)

# @tool("web_search", parse_docstring=True)
@tool
def web_search_new(query: str) -> str:
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
        contents = []
        for r in res["results"]:
            contents.append(r.get("content",""))
        return "\n".join(contents)

    except Exception as e:
        print(e)
        return f"Error: {e}"

# if __name__ == "__main__":
    # print(web_search_new.name)
    # print(web_search_new.description)
    # result = web_search_new.invoke({'query': "机器学习"})
    # print(result)
    # for item in result["results"]:
    #     print(item["content"])