from fastapi import APIRouter, Request

router = APIRouter()


@router.get("/testing/")
async def test(request: Request):
    return {"message": "Wow, test succesful!"}

@router.get("/test/{name}")
async def test_name(request: Request, name: str):
    return {"message": f"Wow, test succesful! {name}"}
