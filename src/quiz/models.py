from datetime import datetime
from typing import Any, Optional, Type
from uuid import uuid4
from sqlalchemy import (TIMESTAMP, Column, MetaData, String, Table, Integer)
from sqlalchemy.orm import registry
from sqlalchemy.orm.mapper import Mapper
from sqlalchemy.sql.selectable import FromClause

metadata: MetaData = MetaData()


quiz: Table = Table(
    'quiz',
    metadata,
    Column('id', Integer, unique=True, nullable=False),
    Column('answer', String(length=320),unique=True, nullable=False),
    Column('question', String(length=1024), nullable=False),
    Column('created_at', String(length=320), nullable=False),
    Column('date_added', TIMESTAMP, default=datetime.utcnow, nullable=False),
)

# class Quiz(registry):
#     def map_imperatively(self, class_, local_table: FromClause | None = None, **kw: Any):
#         return super().map_imperatively(class_, local_table, **kw)
