from app.vacancies.models import Vacancies
from app.dao.base import BaseDAO

class VacanciesDAO(BaseDAO):
    model = Vacancies