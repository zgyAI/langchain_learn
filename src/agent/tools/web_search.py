from langchain_core.tools import tool
from agent.my_llm import openai_llm


@tool("web_search", parse_docstring=True)
def web_search(query:str) -> str:
    """
    互联网搜索工具，可以搜索所有的信息

    Args:
        query: 需要进行互联网查询的信息


    Returns:
        返回搜索的结果信息，该信息
    """
    try:
        res = openai_llm.web_search.web_search(
            search_engine='search_pro',
            search_query=query,
        )
        if res.search_results:
            return "\n\n".join([d.content for d in res.search_results])

    except Exception as e:
        print(e)
        return f"Error: {e}"