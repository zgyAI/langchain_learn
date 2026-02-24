from typing import Type
from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field, create_model
from agents_tools.tools.tool_web_search_new import web_search_new

# 第一种写法
class SearchArgs(BaseModel):
    query: str = Field(..., description="需要进行联网查询的查询信息")

class MyWebSearch(BaseTool):
    name: str = "MyWebSearch"  # 工具的名称
    description: str = "使用这个工具可以进行联网搜索"  # 工具描述

    # 第一种写法
    # args_schema: Type[BaseModel] = SearchArgs  # 工具的参数

    # 第二种写法
    def __init__(self):
        super().__init__()
        self.args_schema = create_model("SearchInput", query=(str, Field(..., description="需要进行联网查询的查询信息")))

    def _run(self, query: str) -> str:
        try:
            response = web_search_new.invoke({"query": query})
            return response

        except Exception as e:
            return str(e)
