from pydantic import BaseModel


class TaskCreate(BaseModel):
    title: str
    description: str = ""
    user: str
    completed: bool = False


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    user: str | None = None
    completed: bool | None = None


class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    user: str
    completed: bool
    
    class Config:
        from_attributes = True
