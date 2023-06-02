from typing import List

import aiohttp
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import Row, select, insert

from src.constants import API_URL, REDIS
from src.quiz.models import quiz
from src.quiz.schemas import QuestionResponse


async def save(values: List[Row], session: AsyncSession):
    """Saves values to database."""
    await session.execute(insert(quiz), values)
    await session.commit()


async def fill_cache(db_session: AsyncSession):
    """Adds all entries from Relation-data-base."""
    query = select(quiz)
    db_request = await db_session.execute(query)
    for entry in db_request.all():
        question = QuestionResponse.from_orm(entry).dict()
        REDIS.set(question['answer'], question['answer'])


async def request_quiz(count: int) -> List[dict]:
    """Request to jservice.io API."""
    async with aiohttp.ClientSession() as session:
        params = {'count': count}
        try:
            async with session.get(url=API_URL, params=params) as response:
                data = await response.json()
                return data
        except aiohttp.ClientConnectorError:
            raise HTTPException(
                status_code=404,
                detail=f"Сервер '{API_URL}' не отвечает!"
            )


def formatted_row(entry: dict):
    return {
        'id': entry['id'],
        'answer': entry['answer'],
        'question': entry['question'],
        'created_at': entry['created_at']
    }


async def validate_exists(entry: dict, validated_data: List[dict]):
    if REDIS.exists(entry['answer']) == 0:
        REDIS.set(entry['answer'], entry['answer'])
        validated_data.append(formatted_row(entry))
        return validated_data


async def fill_quiz(count: int, db_session: AsyncSession):
    """Saves all entries from API request to DataBase."""
    data = await request_quiz(count)
    validated_data = []
    for entry in data:
        await validate_exists(entry, validated_data)
    if len(validated_data) < count:
        await fill_quiz(count - len(validated_data), db_session)
    await save(validated_data, db_session)
