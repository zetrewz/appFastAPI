from datetime import datetime

from sqlalchemy import Column, ForeignKey, DateTime, Integer, UniqueConstraint

from database import Base


class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True)
    applied_at = Column(DateTime, default=datetime.now)
    resume_id = Column(ForeignKey("resumes.id"), nullable=False)
    vacancy_id = Column(ForeignKey("vacancies.id"), nullable=False)

    __table_args__ = (UniqueConstraint("resume_id", "vacancy_id", name="_resume_vacancy_uc"),)
