from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db

from app.features.user.schema import (
    UserCreate,
    UserResponse,
    UserUpdate
)

from app.features.user.service import UserService


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


# Create User
@router.post("/", response_model=UserResponse)
async def create_user(
    user_data: UserCreate,
    db: AsyncSession = Depends(get_db)
):

    service = UserService(db)

    return await service.create_user(user_data)


# Get All Users
@router.get("/", response_model=list[UserResponse])
async def get_all_users(
    db: AsyncSession = Depends(get_db)
):

    service = UserService(db)

    return await service.get_all_users()


# Get One User
@router.get("/{user_id}", response_model=UserResponse)
async def get_one_user(
    user_id: int,
    db: AsyncSession = Depends(get_db)
):

    service = UserService(db)

    return await service.get_one_user(user_id)

# Update User
@router.put("/{user_id}", response_model=UserResponse)
async def update_user(
    user_id: int,
    user_data: UserUpdate,
    db: AsyncSession = Depends(get_db)
):

    service = UserService(db)

    return await service.update_user(
        user_id,
        user_data
    )


# Delete User
@router.delete("/{user_id}")
async def delete_user(
    user_id: int,
    db: AsyncSession = Depends(get_db)
):

    service = UserService(db)

    return await service.delete_user(user_id)