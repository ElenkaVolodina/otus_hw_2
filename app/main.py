from fastapi import FastAPI, HTTPException, APIRouter

from app.schemas.user import User, UserCreate, UserUpdate
from app.utils import user as user_utils

app = FastAPI(
    title="OTUS HomeWork #2",
    version="1",
)


@app.get("/health")
async def root():
    return {"status": "OK"}


router = APIRouter(prefix="/api/v1")


@router.post("/user/", response_model=User)
async def create_user(user: UserCreate):
    db_user = await user_utils.get_user_by_username(username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    user = await user_utils.create_user(user=user)
    return user


@router.get("/user/{user_id}/", response_model=User)
async def read_user(user_id: int):
    db_user = await user_utils.get_user(user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.put("/user/{user_id}/", description='user updated')
async def update_user(user_id: int, user: UserUpdate):
    await user_utils.update_user(user_id, user=user)


@router.delete("/user/{user_id}", status_code=204)
async def delete_user(user_id: int):
    await user_utils.delete_user(user_id=user_id)

app.include_router(router)
