from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.features.todo.schema import (
    TodoCreate,
    TodoUpdate,
    TodoResponse
)
from app.features.todo.service import TodoService


router = APIRouter(
    prefix="/todos",
    tags=["Todos"]
)


# Create Todo
@router.post("/", response_model=TodoResponse)
async def create_todo(
    todo_data: TodoCreate,
    db: AsyncSession = Depends(get_db)
):
    service = TodoService(db)

    return await service.create_todo(todo_data)


# Get All Todos
@router.get("/", response_model=list[TodoResponse])
async def get_all_todos(
    db: AsyncSession = Depends(get_db)
):
    service = TodoService(db)

    return await service.get_all_todos()


# Get One Todo
@router.get("/{todo_id}", response_model=TodoResponse)
async def get_one_todo(
    todo_id: int,
    db: AsyncSession = Depends(get_db)
):
    service = TodoService(db)

    return await service.get_one_todo(todo_id)


# Update Todo
@router.put("/{todo_id}", response_model=TodoResponse)
async def update_todo(
    todo_id: int,
    todo_data: TodoUpdate,
    db: AsyncSession = Depends(get_db)
):
    service = TodoService(db)

    return await service.update_todo(todo_id, todo_data)


# Delete Todo
@router.delete("/{todo_id}")
async def delete_todo(
    todo_id: int,
    db: AsyncSession = Depends(get_db)
):
    service = TodoService(db)

    return await service.delete_todo(todo_id)