from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

from config import settings

DATABASE_URL = (f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASS}"
                f"@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}")

engine = create_async_engine(DATABASE_URL)

async_session = sessionmaker(bind=engine, class_=AsyncSession, autoflush=False, autocommit=False)

Base = declarative_base()
