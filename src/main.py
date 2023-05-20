from fastapi import FastAPI, Depends
from sqlalchemy import desc, select
from sqlalchemy.ext.asyncio import AsyncSession

from quiz.schemas import Question, QuestionResponse
from quiz.models import quiz
from quiz.utils import get_quiz, r
from database import get_async_session

app = FastAPI(
    title='Quiz',
    description='This app, - gives question with answer by using POST request.'
)


@app.post("/quiz")
async def read_root(item: Question,
                    session: AsyncSession = Depends(get_async_session)):
    await get_quiz(count=item.questions_num, db_session=session)
    query = select(quiz).order_by(desc(quiz.c.date_added))
    result = await session.execute(query)
    r.flushall()
    return QuestionResponse.from_orm(result.first())
