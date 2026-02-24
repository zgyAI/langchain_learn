from langchain.agents import create_agent
from agents_tools.my_llm import openai_llm

def send_email(to: str, subject: str, body: str) -> str:
    """
    发送邮件工具。
    参数：
    - to: 收件人邮箱
    - subject: 邮件主题
    - body: 邮件正文
    返回：发送结果说明
    """
    return f'邮件已发送至{to}，主题是{subject}，内容是{body}'

agent = create_agent(
    openai_llm,
    tools=[send_email],
    system_prompt="你是一个邮件助手，请始终使用send_email工具"
)