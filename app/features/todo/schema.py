from pydantic import BaseModel


class TodoCreate(BaseModel):
    title: str
    description: str


class TodoUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None


class TodoResponse(TodoCreate):
    id: int
    completed: bool

    model_config = {
        "from_attributes": True
    }