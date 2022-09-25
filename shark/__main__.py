from datetime import datetime
from loguru import logger
import uvicorn

from shark.constants import Config
from shark.endpoints import testing

from fastapi import FastAPI, Request

app = FastAPI(
    title=Config.TITLE,
    description=Config.DESCRIPTION,
    version=Config.VERSION,
    license_info={
        "name": "MIT license",
        "url": "https://github.com/Dekriel/sharkboard/blob/main/LICENSE",
    },
    redoc_url=None,
    docs_url=None,
)

app.include_router(testing.router, tags=["testing"])


@app.on_event("startup")
async def startup_event():
    logger.debug(f"Server started at: {datetime.now()}")


@app.get("/")
async def root(request: Request):
    return {"message": "Hello World!"}


@app.get("/docs", include_in_schema=False)
async def docs(request: Request):
    return Config.TEMPLATES.TemplateResponse("docs.html", {"request": request}, 200)


if __name__ == "__main__":
    uvicorn.run("shark.__main__:app", host="0.0.0.0", port=5001, reload=True)
