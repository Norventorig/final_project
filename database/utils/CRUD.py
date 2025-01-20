from typing import List, Dict
from database.common.models import *
from peewee import Expression


def _create(model: BaseModel, data: List[Dict]) -> None:
    with db:
        model.insert_many(data).execute()


def _retrieve_all_history() -> List[History]:
    with db:
        all_history = History.select()

    return list(all_history)


def _update(model: BaseModel, changes: dict, conditions: Expression) -> None:
    with db:
        model.update(**changes).where(conditions).execute()


def _delete(model: BaseModel, conditions: Expression) -> None:
    with db:
        model.delete().where(conditions).execute()


class CRUD_interface:
    @staticmethod
    def create(model: BaseModel, data: List[Dict]) -> None:
        return _create(model, data)

    @staticmethod
    def retrieve_all_history() -> List[History]:
        return _retrieve_all_history()

    @staticmethod
    def update(model: BaseModel, changes: dict, conditions: Expression) -> None:
        return _update(model, changes, conditions)

    @staticmethod
    def delete(model: BaseModel, conditions: Expression) -> None:
        return _delete(model, conditions)
