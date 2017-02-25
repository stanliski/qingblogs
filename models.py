#! /usr/bin/env python
from peewee import *
from playhouse.db_url import connect
from playhouse.shortcuts import *
import datetime
from settings import *

db = SqliteDatabase(SQLITE_URL)

class BaseModel(Model):
    class Meta:
        dabtabase = db

class UserGroup(BaseModel):
    name = CharField(default='', unique=True)
    class Meta:
        db_table = 'user_group'

class User(BaseModel):
    user_group = ForeignKeyField(UserGroup, on_update='CASCADE', on_delete='CASCADE')
    name = CharField(unique=False)
    email = CharField(index=True, unique=True)
    indro = TextField(default='')
    admin = BooleanField(default=True)
    phone_number = CharField(default='')
    created_at = DateTimeField(default=datetime.datetime.now)
    class Meta:
        db_table = 'user'

class Settings(BaseModel):
    editor_theme = CharField()
    sync_youdao = BooleanField(default=False)
    sync_evernote = BooleanField(default=False)
    bg_img = CharField(default="")
    blog_theme = CharField(default='')
    markdown_theme = CharField(default='')
    class Meta:
        db_table = 'settings'

class Tag(BaseModel):
    user = ForeignKeyField(User, on_update='CASCADE', on_delete='CASCADE')
    content = CharField(unique=True)
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        db_table = 'tag'

    def to_json(self):
        return {
            'id': self.id,
            'user': self.user.name,
            'content': self.content,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S')
        }

class Notify(BaseModel):
    user = ForeignKeyField(User, on_update='CASCADE', on_delete='CASCADE')
    content = TextField(default='')
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        db_table = 'notify'

    def to_json(self):
        return {
            'id': self.id,
            'user': self.user.name,
            'content': self.content,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }

class Post(BaseModel):
    user = ForeignKeyField(User, on_update='CASCADE', on_delete='CASCADE')
    title = CharField(unique=True)
    content = TextField(default='')
    status = IntegerField(default=0) # 0 publish, 1 hide, 2 trash
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        db_table = 'post'

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'status': self.status,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': self.updated_at.strftime('%Y-%m-%d %H:%M:%S')
        }

class PostTags(BaseModel):
    post = ForeignKeyField(Post)
    tag = ForeignKeyField(Tag)
    class Meta:
        db_table = 'post_tags'

class History(BaseModel):
    content = CharField(default='')
    create_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        db_table = 'history'

    def to_json(self):
        return {
            'id': self.id,
            'content': self.content,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }

def create_tables():
    db.create_tables([User, Settings, Post, Tag, UserGroup, Notify, History, PostTags], safe=True)

if __name__ == '__main__':
    create_tables()
