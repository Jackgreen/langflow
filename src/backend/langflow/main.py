import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from langflow.api import router
from langflow.database.base import create_db_and_tables

os.environ["http_proxy"] = "http://10.105.16.23:7890"
os.environ["https_proxy"] = "http://10.105.16.23:7890"


def create_app():
    """Create the FastAPI app and include the router."""

    app = FastAPI()

    origins = [
        "*",
    ]

    @app.get("/health")
    def get_health():
        return {"status": "OK"}

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(router)
    app.on_event("startup")(create_db_and_tables)
    return app


app = create_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="10.105.16.24", port=7860)
