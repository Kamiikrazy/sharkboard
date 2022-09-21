from datetime import datetime
from loguru import logger
import uvicorn

from shark.constants import Server

from fastapi import FastAPI, Request

app = FastAPI(redoc_url=None, docs_url=None)


@app.on_event("startup")
async def startup_event():
    logger.debug(f"Server starting at: {datetime.now()}")


@app.get("/")
async def root(request: Request):
    return {"message": "Hello World!"}

@app.get("/test/")
async def test(request: Request):
    return {"message": "Wow, test succesful!"}

@app.get("/test/{name}")
async def test_name(request: Request, name: str):
    return {"message": f"Wow, test succesful! {name}"}

@app.get("/docs", include_in_schema=False)
async def docs(request: Request):
    return Server.TEMPLATES.TemplateResponse("docs.html", {"request": request}, 200)


if __name__ == "__main__":
    uvicorn.run("shark.__main__:app", host="127.0.0.1", port=5001, reload=True)
