from fastapi import FastAPI, Depends
from pydantic import ValidationError
from sqlalchemy import desc, select
from sqlalchemy.ext.asyncio import AsyncSession

from quiz.schemas import Question, QuestionResponse
from quiz.models import quiz
from quiz.utils import get_quiz
from database import get_async_session
from constants import REDIS, APP_DESCRITION

app = FastAPI(
    title='Quiz',
    description=APP_DESCRITION
)


@app.post("/quiz", response_model=QuestionResponse)
async def read_root(item: Question,
                    session: AsyncSession = Depends(get_async_session)):
    await get_quiz(count=item.questions_num, db_session=session)
    query = select(quiz).order_by(desc(quiz.c.date_added))
    result = await session.execute(query)
    REDIS.flushall()
    try:
        return QuestionResponse.from_orm(result.first())
    except ValidationError:
        return {}
