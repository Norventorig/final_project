from typing import List, Dict, TypeVar
from database.common.models import *
from peewee import Expression


T = TypeVar('T')


def _create(model: T, data: List[Dict]) -> None:
    with db:
        model.insert_many(data).execute()


def _retrieve_all_history() -> List[History]:
    with db:
        all_history = History.select()

    return list(all_history)


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
    def retrieve_all_history() -> List[History]:
        return _retrieve_all_history()

    @staticmethod
    def update(model: T, changes: dict, conditions: Expression) -> None:
        return _update(model, changes, conditions)

    @staticmethod
    def delete(model: T, conditions: Expression) -> None:
        return _delete(model, conditions)
