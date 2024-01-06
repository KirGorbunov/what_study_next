from fastapi import APIRouter


router = APIRouter(
    prefix="/vacancies",
    tags=["Vacancies"],
)


@router.get("")
def get_vacancies():
    pass