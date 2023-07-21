from typing import Any, List, Mapping, Optional

import requests
from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import LLM

url_dict = {"baichuan-chat13b": "http://10.105.16.23:8000","chatglm-chat6b":"http://10.105.16.23:2025"}


class CustomLLM(LLM):
    temperature: float = 1
    top_p: float = 0.75
    type: str = 'chatglm-chat13b'

    @property
    def _llm_type(self) -> str:
        return "custom"

    def _call(
            self,
            prompt: str,
            stop: Optional[List[str]] = None,
            run_manager: Optional[CallbackManagerForLLMRun] = None,
            **kwargs: Any,
    ) -> str:
        if stop is not None:
            raise ValueError("stop kwargs are not permitted.")
        dt = {
            "prompt": prompt,
            "history": [],
            "temperature": self.temperature,
            "top_p": self.top_p
        }
        message = {}
        try:
            url = url_dict[self.type]
            x = requests.post(url, json=dt, verify=False, timeout=1000)
            message = x.json()['response']
            return message
        except Exception as e:
            message = str(e)
        finally:
            return message

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {"temperature": self.temperature, "top_p": self.top_p, }
