from agents_tools.tools.tool_web_search_new import web_search_new
from langchain.agents import create_agent
from agents_tools.my_llm import openai_llm

agent = create_agent(
    openai_llm,
    tools=[web_search_new],
    system_prompt="你是一个智能助手，尽可能调用工具回答用户问题"
)