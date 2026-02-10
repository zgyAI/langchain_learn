from langchain.agents import create_agent

def send_email(to: str, subject: str, body: str):
    email = {"to": to, "subject": subject, "body": body}
    return f'邮件已发送至{to}'

agent = create_agent(
    "deepseek-ai/DeepSeek-V3.2",
    tools=[send_email],
    system_prompt="你是一个邮件助手，请始终使用send_email工具"
)