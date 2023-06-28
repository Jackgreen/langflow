import base64
import logging
from typing import List

import requests
from langchain.docstore.document import Document
from langchain.document_loaders import TextLoader

logger = logging.getLogger(__name__)


class CommonFileLoader(TextLoader):
    """Load common files.
    """
    name = "common_file_loader"
    description = ""

    def __init__(self, file_path: str, algo_type: str, file_type: str):
        """Initialize with file path."""
        super().__init__(file_path)
        self.file_path = file_path
        self.algo_type = algo_type
        self.file_type = file_type

    def load(self) -> List[Document]:
        """Load from file path."""
        text = ""
        try:
            # 读取文件内容
            with open(self.file_path, "rb") as f:
                base64_data = base64.b64encode(f.read()).decode("utf8")
            data = {"data": base64_data, "ext": self.file_type}
            # 请求内部算法
            text = requests.post("http://10.105.16.21:8081/" + self.algo_type, json=data).text
            # 解析结果

        except Exception as e:
            raise RuntimeError(f"invoke {self.algo_type} service failed") from e
            # text = f"invoke {self.algo_type} service failed"

        metadata = {"source": self.file_path}
        return [Document(page_content=text, metadata=metadata)]
