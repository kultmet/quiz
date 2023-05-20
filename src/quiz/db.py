# from datetime import datetime
# from uuid import uuid4

# from database import Base, get_async_session
# # from fastapi import Depends
# # from fastapi_users.db import (SQLAlchemyBaseUserTableUUID,
# #                               SQLAlchemyUserDatabase)
# from sqlalchemy import TIMESTAMP, UUID, Boolean, Column, String
# from sqlalchemy.ext.asyncio import AsyncSession

# # from .mail import get_verification_code


# class User(Base):
#     id: Column[UUID] = Column(
#         UUID(as_uuid=True), primary_key=True, default=uuid4, index=True)
#     email: Column[str] = Column(
#         String(length=320), unique=True, index=True, nullable=False)
#     hashed_password: Column[str] = Column(String(length=1024), nullable=False)
#     bio: Column[str] = Column(String, nullable=True)
#     is_active: Column[bool] = Column(Boolean, default=True, nullable=False)
#     is_superuser: Column[bool] = Column(Boolean, default=False, nullable=False)
#     is_verified: Column[bool] = Column(Boolean, default=False, nullable=False)
#     added: Column[datetime] = Column(TIMESTAMP, default=datetime.utcnow)


# async def get_user_db(session: AsyncSession = Depends(get_async_session)):
#     yield SQLAlchemyUserDatabase(session, User)