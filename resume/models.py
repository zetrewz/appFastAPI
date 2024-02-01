from sqlalchemy import Column, String, ForeignKey, Integer

from database import Base


class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    work_name = Column(String, nullable=False)
    about = Column(String, nullable=False)
    user_id = Column(ForeignKey("users.id"), nullable=False)
