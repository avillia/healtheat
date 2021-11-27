from enum import Enum


class MyEnum(str, Enum):
    @classmethod
    def values(cls) -> list[str]:
        return list(cls._member_map_.keys())


class Roles(MyEnum):
    user = "user"
    doctor = "doctor"
    moder = "moder"
    admin = "admin"
