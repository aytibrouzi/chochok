from peewee import * 
import datetime 
from  flask_login import UserMixin

db = PostgresqlDatabase(
    'thewe',
    host = 'localhost',
    port = 5432,
    user = 'the_the',
    password = 'qwe123'
)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db
    
    
class Users(BaseModel, UserMixin):
    email = CharField(max_length=225, null = False, unique = True)
    name = CharField(max_length=225, null = False)
    password = CharField(max_length=225, null = False)

    def repr(self):
        return self.email
    
class Post(BaseModel):
    author = ForeignKeyField(Users, on_delete='CASCADE')
    title = CharField(max_length=225, null = False)
    phone_number = TextField()
    description = TextField()
    date = DateTimeField(default=datetime.datetime.now)

    def repr(self):
        return self.title    

class Like(BaseModel, UserMixin):
    post_id = ForeignKeyField(Post, on_delete='CASCADE')
    num_like = IntegerField()

    def repr(self):
        return self.num_like

db.create_tables([Users, Post, Like])
