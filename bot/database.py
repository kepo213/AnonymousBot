from peewee import SqliteDatabase, Model, CharField, IntegerField, BooleanField
import asyncio

conn = SqliteDatabase("database.db")


class BaseModel(Model):
    class Meta:
        database = conn  # соединение с базой, из шаблона выше


class User(BaseModel):
    user_id = CharField(unique=True)
    username = CharField()
    reputation = IntegerField(default=100)
    opponent_id = CharField(null=True)
    waiting = BooleanField(default=False)
    banned = BooleanField(default=False)

    class Meta:
        table_name = 'user'


class Main_information(BaseModel):
    field = CharField()
    value = IntegerField(default=0)

    class Meta:
        table_name = "main_information"


def init_main_information():
    Main_information.create_table()
    User.create_table()
    if not Main_information.select().where(Main_information.field == "count_users"):
        Main_information.create(field="count_users")
    if not Main_information.select().where(Main_information.field == "good_requests"):
        Main_information.create(field="good_requests")


def add_user(user_id, username):
    if User.select().where(User.user_id == user_id).exists():
        return
    User.create(user_id=user_id, username=username)
    query = Main_information.update(value=Main_information.value+1).where(Main_information.field == "count_users")
    query.execute()


def get_opponent_id(user_id):
    user = User.get(user_id=user_id)
    return user.opponent_id


def search_opponent(user_id):
    users = User.select().where(User.user_id != user_id and User.waiting == True)
    if users.exists():
        return users.get().user_id
    query = User.update(waiting=True).where(User.user_id == user_id)
    query.execute()


def end_waiting(user_id):
    user = User.get(user_id=user_id)
    user.waiting = False
    user.save()


def set_opponent(user_id, opponent_id):
    user = User.get(user_id=user_id)
    user.opponent_id = opponent_id
    user.save()
    opponent = User.get(user_id=opponent_id)
    opponent.opponent_id = user_id
    opponent.save()


def delete_opponent(user_id, opponent_id):
    user = User.get(user_id=user_id)
    user.opponent_id = None
    user.save()
    opponent = User.get(user_id=opponent_id)
    opponent.opponent_id = None
    opponent.save()
