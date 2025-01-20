from database.utils.CRUD import CRUD_interface
from database.common.models import User, History, db


db.connect()
db.create_tables([User, History])

crud = CRUD_interface
