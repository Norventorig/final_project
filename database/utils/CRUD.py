from typing import List, Dict, TypeVar
from database.common.models import *
from peewee import Expression


T = TypeVar('T')


def _create(model: T, data: List[Dict]) -> None:
    with db:
        model.insert_many(data).execute()


def _retrieve(model: T, conditions: Expression) -> List[BaseModel]:
    with db:
        data = model.select().where(conditions).execute()

    return list(data)


def _update(model: T, changes: dict, conditions: Expression) -> None:
    with db:
        model.update(**changes).where(conditions).execute()


def _delete(model: T, conditions: Expression) -> None:
    with db:
        model.delete().where(conditions).execute()


class CRUD_interface:
    @staticmethod
    def create(model: T, data: List[Dict]) -> None:
        return _create(model, data)

    @staticmethod
    def retrieve(model: T, conditions: Expression) -> List[BaseModel]:
        return _retrieve(model, conditions)

    @staticmethod
    def update(model: T, changes: dict, conditions: Expression) -> None:
        return _update(model, changes, conditions)

    @staticmethod
    def delete(model: T, conditions: Expression) -> None:
        return _delete(model, conditions)
