from basedao.base import BaseDAO
from service.models import Application


class ApplicationDAO(BaseDAO):
    model = Application
