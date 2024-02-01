from datetime import datetime

from sqlalchemy import Column, Boolean, String, ForeignKey, DateTime, Integer

from database import Base


class Vacancy(Base):
    __tablename__ = "vacancies"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True, nullable=False)
    company_name = Column(String, nullable=False)
    about = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    is_active = Column(Boolean, default=True)
    user_id = Column(ForeignKey("users.id"), nullable=False)
