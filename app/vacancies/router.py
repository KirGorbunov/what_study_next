from fastapi import APIRouter
from app.vacancies.dao import VacanciesDAO


router = APIRouter(
    prefix="/vacancies",
    tags=["Vacancies"],
)


@router.get("")
async def get_vacancies():
    return await VacanciesDAO.find_all()