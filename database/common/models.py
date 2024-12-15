from peewee import *
import datetime


db = SqliteDatabase('tg_bot.db')


class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order_by = 'id'


class User(BaseModel):
    chat_id = CharField(max_length=9)
    user_name = CharField(max_length=30)
    name = CharField(max_length=20)
    last_name = CharField(max_length=20, default=None)

    class Meta:
        db_table = 'users'


class History(BaseModel):
    query_body = CharField(max_length=255)
    author = ForeignKeyField(User)
    date = DateField(default=datetime.datetime.today())

    class Meta:
        db_table = 'histories'
