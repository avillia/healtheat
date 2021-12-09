from enum import Enum


class Roles(str, Enum):
    user = "user"
    doctor = "doctor"
    moder = "moder"
    admin = "admin"
