from sqlalchemy import Column, Integer, String, Boolean

from database import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(String(500), nullable=True)
    user = Column(String(100), nullable=False)
    completed = Column(Boolean, default=False)