from datetime import datetime

from pydantic import BaseModel, Field


class Question(BaseModel):
    questions_num: int = Field(ge=1)


class QuestionResponse(BaseModel):
    id: int
    question: str
    answer: str
    created_at: datetime
    date_added: datetime

    class Config:
        orm_mode = True
