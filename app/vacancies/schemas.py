from datetime import date

from pydantic import BaseModel


class SVacancies(BaseModel):
    id: int
    name: str
    published_at: date
    skills: list
    actual: bool