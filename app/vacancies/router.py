from fastapi import APIRouter
from app.vacancies.dao import VacanciesDAO
from app.vacancies.schemas import SVacancies

router = APIRouter(
    prefix="/vacancies",
    tags=["Vacancies"],
)


@router.get("")
async def get_vacancies() -> list[SVacancies]:
    return await VacanciesDAO.find_all()