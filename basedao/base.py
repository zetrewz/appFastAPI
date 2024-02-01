from fastapi import HTTPException
from sqlalchemy import select, insert, delete

from database import async_session
from exceptions import ObjectDoesNotExist


class BaseDAO:
    model = None

    @classmethod
    async def get_object_or_none(cls, **filter_by):
        async with async_session() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def get_object_or_exception(cls, **filter_by):
        existing_object = await cls.get_object_or_none(**filter_by)
        if existing_object is None:
            raise ObjectDoesNotExist

        return existing_object

    @classmethod
    async def get_objects(cls, **filter_by):
        async with async_session() as session:
            query = select(cls.model).filter_by(**filter_by)
            objects = await session.execute(query)
            return objects.scalars().all()

    @classmethod
    async def add(cls, **data):
        async with async_session() as session:
            new_object = cls.model(**data)
            session.add(new_object)

            await session.commit()
            await session.refresh(new_object)
            return new_object

    @classmethod
    async def update(cls, object_id: int, **data):
        async with async_session() as session:
            existing_object = await cls.get_object_or_exception(id=object_id)

            for key, value in data.items():
                if hasattr(existing_object, key):
                    setattr(existing_object, key, value)

            await session.commit()
            await session.refresh(existing_object)
            return existing_object

    @classmethod
    async def delete(cls, object_id: int):
        async with async_session() as session:
            existing_object = await cls.get_object_or_exception(id=object_id)

            query = delete(cls.model).where(cls.model.id == object_id)
            await session.execute(query)
            await session.commit()
