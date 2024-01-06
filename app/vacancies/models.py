from sqlalchemy import JSON, Column, Integer, String, ForeignKey, Date, ARRAY, Boolean
from app.database import Base

class Vacancies(Base):
    __tablename__ = "vacancies"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    published_at = Column(Date, nullable=False)
    skills = Column(ARRAY(String), nullable=True)
    actual = Column(Boolean, nullable=False)