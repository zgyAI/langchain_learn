# from agents_tools.tools.tool_web_search_old import web_search_old
from agents_tools.tools.tool_web_search_new import web_search_new
from langchain_core.prompts import ChatPromptTemplate
from agents_tools.my_llm import openai_llm

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个信息分析助手。你会基于提供的搜索结果做总结：只用结果中出现的信息，不要编造。输出中文。"),
    ("user",
     "用户问题：{query}\n\n"
     "搜索结果：\n{search_text}\n\n"
     "请输出：\n"
     "1) 3-6条要点总结（每条<=50字）\n"
     "2) 一段150-300字的综合概述\n"
     "3) 你引用了哪些条目编号（如1,3,5）")
])

def search_and_summarize(query: str) -> str:
    search_text = web_search_new.invoke({"query": query})
    return openai_llm.invoke(prompt.format_messages(query=query, search_text=search_text)).content

if __name__ == "__main__":
    print(search_and_summarize("介绍一下机器学习"))