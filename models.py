#! /usr/bin/env python
from peewee import *
from playhouse.db_url import connect
from playhouse.shortcuts import *
import datetime
from settings import *
from werkzeug.security import generate_password_hash, check_password_hash

DATABASE = SqliteDatabase(SQLITE_URL)


class BaseModel(Model):

    class Meta:
        dabtabase = DATABASE

class User(BaseModel):
    username = CharField(unique=True)
    mail = CharField(unique=True, default='')
    password_hash = CharField(max_length=128)
    indro = TextField(default='')
    admin = BooleanField(default=True)
    phone_number = CharField(default='')
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        db_table = 'user'

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.user.name,
            'mail': self.mail,
            'intro': self.intro,
            'phone_number': self.phone_number,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }


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
    title = CharField(default='')
    content = TextField(default='')
    status = IntegerField(default=0)  # 0 publish, 1 hide, 2 trash
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
    DATABASE.create_tables(
        [User, Settings, Post, Tag, Notify, History, PostTags], safe=True)

if __name__ == '__main__':
    create_tables()
    user = User.create(username='stanley',
                       mail='1015757334@qq.com', password='123')
    user.save()
