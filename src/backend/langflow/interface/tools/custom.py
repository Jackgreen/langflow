from typing import Callable, Optional

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


class PoliceAnalyse(BaseTool):
    """Tool for making a POST request to an API endpoint."""
    name = "police_analyse"
    description = ""
    tool_type: str

    def gettext(self, text: str, type: str) -> str:
        # 解析结果
        if type in ["rules"]:
            result = "涉案金额大于等于3000为刑事案件，小于3000为治安案件"
        else:
            result = "刑事案件##诈骗案   治安案件,治安案件##诈骗"
        return result

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
            self.type_result = "涉案金额大于等于3000为刑事案件，小于3000为治安案件"
            return result
        except Exception as e:
            return repr(e)
