from basedao.base import BaseDAO
from resume.models import Resume


class ResumeDAO(BaseDAO):
    model = Resume
