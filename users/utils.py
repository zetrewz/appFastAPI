from enum import Enum


class UserTypeChoices(str, Enum):
    worker = "worker"
    employer = "employer"
