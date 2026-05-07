from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException

from app.db.model import Todo
from app.features.todo.schema import TodoCreate, TodoUpdate


class TodoService:
    def __init__(self, db: AsyncSession):
        self.db = db

    # Create Todo
    async def create_todo(self, todo: TodoCreate):
        db_todo = Todo(**todo.model_dump())
        self.db.add(db_todo)
        await self.db.commit()
        await self.db.refresh(db_todo)
        return db_todo

    # Get All Todos
    async def get_all_todos(self):
        result = await self.db.execute(
            select(Todo)
        )

        return result.scalars().all()

    # Get Single Todo
    async def get_one_todo(self, todo_id: int):
        todo = await self.db.get(Todo, todo_id)

        if not todo:
            raise HTTPException(
                status_code=404,
                detail="Todo not found"
            )

        return todo

    # Update Todo
    async def update_todo(self, todo_id: int, todo_data: TodoUpdate):
        todo = await self.db.get(Todo, todo_id)

        if not todo:
            raise HTTPException(
                status_code=404,
                detail="Todo not found"
            )

        update_data = todo_data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(todo, key, value)

        await self.db.commit()
        await self.db.refresh(todo)

        return todo

    # Delete Todo
    async def delete_todo(self, todo_id: int):
        todo = await self.db.get(Todo, todo_id)

        if not todo:
            raise HTTPException(
                status_code=404,
                detail="Todo not found"
            )

        await self.db.delete(todo)
        await self.db.commit()

        return {
            "message": "Todo deleted successfully"
        }