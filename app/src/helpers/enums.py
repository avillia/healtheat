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

    @classmethod
    def generate_permissions(cls) -> list[dict]:
        boolean_flags = ("can_manage_users_data", "can_manage_medical_info")
        return [
            {"name": role, **dict(zip(boolean_flags, [int(i) for i in f"{index:02b}"]))}
            for index, role in enumerate(cls.values())
        ]
