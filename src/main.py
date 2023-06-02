from fastapi import FastAPI, Depends
from pydantic import ValidationError
from sqlalchemy import desc, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.quiz.schemas import Question, QuestionResponse
from src.quiz.models import quiz
from src.quiz.utils import fill_cache, fill_quiz
from src.database import get_async_session
from src.constants import REDIS, APP_DESCRITION

app = FastAPI(
    title='Quiz',
    description=APP_DESCRITION
)


@app.post("/quiz", response_model=QuestionResponse)
async def get_quiz(item: Question,
                   session: AsyncSession = Depends(get_async_session)):
    """Get quiz API view."""
    await fill_cache(session)
    await fill_quiz(count=item.questions_num, db_session=session)
    query = select(quiz).order_by(desc(quiz.c.date_added))
    result = await session.execute(query)
    REDIS.flushall()
    try:
        return QuestionResponse.from_orm(result.first())
    except ValidationError:
        return {}
