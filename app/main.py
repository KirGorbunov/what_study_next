from fastapi import FastAPI, Query, Depends
from datetime import date
from pydantic import BaseModel

from app.vacancies.router import router as router_vacancies
from app.users.router import router as router_users


app = FastAPI()

app.include_router(router_users)
app.include_router(router_vacancies)


class SVacancy(BaseModel):
    name: str
    area: str
    published_at: date
    skills: list
    actual: bool


class SVacanciesSearchArgs:
    def __init__(
        self,
        name: str | None = None,
        area: str | None = None,
        published_at: date | None = None,
        skills: list | None = None,
        actual: bool | None = None,
    ):
        self.name = name
        self.area = area
        self.published_at = published_at
        self.skills = skills
        self.actual = actual


# @app.get("/vacancies")
# def get_vacancies(
#         search_args: SVacanciesSearchArgs = Depends()
# ) -> list[SVacancy]:
#     vacancies = [
#         {
#             "name": "Разработчик Python",
#             "area": "Москва",
#             "published_at": '2023-12-12',
#             "skills": ['Python', 'Javascript'],
#             "actual": True,
#         }
#     ]
#     return vacancies