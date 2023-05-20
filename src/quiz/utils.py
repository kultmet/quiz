from typing import List

import aiohttp
import redis
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import Row, select, insert

from quiz.models import quiz
from quiz.schemas import QuestionResponse

r = redis.Redis(host='localhost', port=6379, decode_responses=True)


async def save(values: List[Row], session: AsyncSession):
    await session.execute(insert(quiz), values)
    await session.commit()


async def fill_cache(db_session: AsyncSession):
    """Adds all entries from Relation-data-base."""
    query = select(quiz)
    db_request = await db_session.execute(query)
    for entry in db_request.all():
        question = QuestionResponse.from_orm(entry).dict()
        r.set(question['answer'], question['answer'])


async def request_quiz(count: int) -> List[dict]:
    """Request to jservice.io API."""
    async with aiohttp.ClientSession() as session:
        url = 'https://jservice.io/api/random'
        params = {'count': count}
        async with session.get(url=url, params=params) as response:
            data = await response.json()
            return data


def formatted_row(entry: dict):
    return {
        'id': entry['id'],
        'answer': entry['answer'],
        'question': entry['question'],
        'created_at': entry['created_at']
    }

async def validate_exists(entry: dict, validated_data: List[dict]):
    if r.exists(entry['answer']) == 1:
        request = await request_quiz(1)
        await validate_exists(request[0], validated_data)
    else:
        r.set(entry['answer'], entry['answer'])
        validated_data.append(formatted_row(entry))
        return validated_data


async def get_quiz(count: int, db_session: AsyncSession):
    """Saves all entries from API request to DataBase."""
    await fill_cache(db_session)
    data = await request_quiz(count)
    validated_data = []
    for entry in data:
        await validate_exists(entry, validated_data)
    await save(validated_data, db_session)
