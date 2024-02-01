from basedao.base import BaseDAO
from vacancy.models import Vacancy


class VacancyDAO(BaseDAO):
    model = Vacancy
