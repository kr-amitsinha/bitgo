from fastapi import FastAPI
from api import api_router
import uvicorn


def create_app() -> FastAPI:
    app = FastAPI(
        title="Bitgo notifier",
        docs_url="/",
        openapi_url="/openapi.json",
    )
    app.include_router(api_router)

    return app

if __name__ == "__main__":
    # noinspection PyTypeChecker
    uvicorn.run(create_app(), host="0.0.0.0")


