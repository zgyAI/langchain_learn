from pathlib import Path
from langchain_deepseek import ChatDeepSeek
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

Base_DIR = Path(__file__).resolve().parents[2]
env_path = Base_DIR / ".env"
load_dotenv(env_path)
api_base = os.environ.get("OPENAI_API_BASE")
api_key = os.environ.get("OPENAI_API_KEY")

openai_llm = ChatOpenAI(
    model="deepseek-ai/DeepSeek-V3.2",
    base_url=api_base,
    api_key=api_key,
    temperature=0.6
)

deepseek_llm = ChatDeepSeek(
    model="deepseek-ai/DeepSeek-R1",
    api_base=api_base,
    api_key=api_key,
    temperature=0.6
)

grok_llm = ChatOpenAI(
    model="grok-4",
    base_url=api_base,
    api_key=api_key,
    temperature=0.6
)

# res = openai_llm.invoke("你是什么模型")
# res = deepseek_llm.invoke("用三句话给我分析一下机器学习")
# res = grok_llm.invoke("给我分析一下美国政府情况")
# print(type(res))
# print(res.content)