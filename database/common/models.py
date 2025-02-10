from peewee import *
import datetime


db = SqliteDatabase('tg_bot.db')


class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order_by = 'id'


class User(BaseModel):
    chat_id = PrimaryKeyField(unique=True)
    user_name = CharField(max_length=30, null=False)
    name = CharField(max_length=20, null=False)
    last_name = CharField(max_length=20, null=True)

    class Meta:
        db_table = 'users'


class History(BaseModel):
    query_body = CharField(max_length=255, null=False)
    author = ForeignKeyField(User)
    date = DateField(default=datetime.datetime.today())

    class Meta:
        db_table = 'histories'
