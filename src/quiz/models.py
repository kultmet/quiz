from datetime import datetime
from sqlalchemy import TIMESTAMP, Column, MetaData, String, Table, Integer

metadata: MetaData = MetaData()


quiz: Table = Table(
    'quiz',
    metadata,
    Column('id', Integer, unique=True, nullable=False),
    Column('answer', String(length=320), unique=True, nullable=False),
    Column('question', String(length=1024), nullable=False),
    Column('created_at', String(length=320), nullable=False),
    Column('date_added', TIMESTAMP, default=datetime.utcnow, nullable=False),
)
