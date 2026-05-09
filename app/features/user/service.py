from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException

from app.db.model import User
from app.features.user.schema import UserCreate, UserUpdate


class UserService:
    def __init__(self, db: AsyncSession):
        self.db = db

    # Create User
    async def create_user(self, user: UserCreate):

        db_user = User(**user.model_dump())

        self.db.add(db_user)

        await self.db.commit()

        await self.db.refresh(db_user)

        return db_user

    # Get All Users
    async def get_all_users(self):

        result = await self.db.execute(
            select(User)
        )

        return result.scalars().all()

    # Get One User
    async def get_one_user(self, user_id: int):

        user = await self.db.get(User, user_id)

        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        return user

    
    # Update User
    async def update_user(
        self,
        user_id: int,
        user_data: UserUpdate
        ):

        user = await self.db.get(User, user_id)

        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        update_data = user_data.model_dump(
        exclude_unset=True
     )

        for key, value in update_data.items():
            setattr(user, key, value)

        await self.db.commit()

        await self.db.refresh(user)

        return user


    # Delete User
    async def delete_user(self, user_id: int):

        user = await self.db.get(User, user_id)

        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        await self.db.delete(user)

        await self.db.commit()

        return {
            "message": "User deleted successfully"
        }