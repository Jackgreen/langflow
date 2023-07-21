from typing import Callable, Optional

import requests
from langchain.callbacks.manager import CallbackManagerForToolRun, AsyncCallbackManagerForToolRun
from langchain.tools import BaseTool

from langflow.interface.importing.utils import get_function

from pydantic import BaseModel, validator

from langflow.utils import validate
from langchain.agents.tools import Tool


class Function(BaseModel):
    code: str
    function: Optional[Callable] = None
    imports: Optional[str] = None

    # Eval code and store the function
    def __init__(self, **data):
        super().__init__(**data)

    # Validate the function
    @validator("code")
    def validate_func(cls, v):
        try:
            validate.eval_function(v)
        except Exception as e:
            raise e

        return v

    def get_function(self):
        """Get the function"""
        function_name = validate.extract_function_name(self.code)

        return validate.create_function(self.code, function_name)


class PythonFunctionTool(Function, Tool):
    name: str = "Custom Tool"
    description: str
    code: str

    def ___init__(self, name: str, description: str, code: str):
        self.name = name
        self.description = description
        self.code = code
        self.func = get_function(self.code)
        super().__init__(name=name, description=description, func=self.func)


class PythonFunction(Function):
    code: str


def get_inner_algo_result(text):
    dt = {
        "input": text
    }
    message = {}
    try:
        x = requests.post('http://10.105.16.23:2023/search', json=dt, verify=False, timeout=1000)
        message = x.json()
        return message
    except Exception as e:
        message = str(e)
    finally:
        return message


class InnerAlgo(BaseTool):
    """Tool for making a POST request to an API endpoint."""
    name = "inner_algo"
    description = "inner algo"
    tool_type: str

    def ___init__(self, name: str, description: str, tool_type: str):
        self.name = name
        self.description = description
        self.tool_type = tool_type
        super().__init__(name=name, description=description)

    def gettext(self, text: str, type: str) -> str:
        # 解析结果
        result = get_inner_algo_result(text)
        labels = result['labels']
        return "  ".join(labels)

    def _run(
            self, text: str, run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        """Run the tool."""
        try:
            # 读取文件内容
            result = get_inner_algo_result(text)
            return result
        except Exception as e:
            return repr(e)

    async def _arun(
            self,
            text: str,
            run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Run the tool asynchronously."""
        try:
            result = text + "hahaha"
            return result
        except Exception as e:
            return repr(e)


def get_mapping_tools_result(text):
    dt = {
        "input": text
    }
    message = {}
    try:
        x = requests.post('http://10.105.16.23:2024/search', json=dt, verify=False, timeout=1000)
        message = x.json()
        return message
    except Exception as e:
        message = str(e)
    finally:
        return message


class MappingTool(BaseTool):
    """Tool for making a POST request to an API endpoint."""
    name = "mapping_tool"
    description = "mapping tool"
    tool_type: str

    def ___init__(self, name: str, description: str, tool_type: str):
        self.name = name
        self.description = description
        self.tool_type = tool_type
        super().__init__(name=name, description=description)

    def gettext(self, text: str, type: str) -> str:
        # 解析结果
        algo_result = get_inner_algo_result(text)
        result = get_mapping_tools_result(algo_result)
        return result['result']

    def _run(
            self, text: str, run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> str:
        """Run the tool."""
        try:
            # 读取文件内容
            result = text + "hahaha"

            return result
        except Exception as e:
            return repr(e)

    async def _arun(
            self,
            text: str,
            run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Run the tool asynchronously."""
        try:
            result = text + "hahaha"
            return result
        except Exception as e:
            return repr(e)
