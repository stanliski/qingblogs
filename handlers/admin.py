# coding: utf-8
import tornado.web

from tornado import gen
from models import *
import peewee
from peewee import fn
from peewee import RawQuery
from .common import BaseRequestHandler
import utils
from auth import *


class FindPasswdHandler(BaseRequestHandler):

    def get(self):
        self.render('admin/account/forgetpasswd.html')


class LoginHandler(BaseRequestHandler):

    def get(self):
        self.render('admin/account/login.html')

    def post(self):
        username = self.get_argument('username', None)
        password = self.get_argument('password', None)
        if (not username) or (not password):
            self.write(
                {'success': False, 'message': "input content is not allow to be empty"})
            return
        try:
            user = User.get((User.username == username)
                            | (User.mail == username))
            if user.verify_password(password):
                self.session.set('user', user)
                self.write({'success': True, 'message': 'login success'})
            else:
                self.write(
                    {'success': False, 'message': 'password is not right'})
        except Exception, e:
            self.write({'success': False, 'message': str(e)})
            return


class LogoutHandler(BaseRequestHandler):

    def get(self):
        self.session.set('user', None)
        self.redirect('/admin/login')


class RegisterHandler(BaseRequestHandler):

    def get(self):
        self.render('admin/account/register.html')

    def post(self):
        username = self.get_argument('username', None)
        password = self.get_argument('password', None)
        mail = self.get_argument('mail', None)
        if (not username) and (not password) and (not mail):
            self.write(
                {'success': False, 'message': 'input content is not allow to be empty'})
            return
        else:
            try:
                query = User.select().where((User.username == username) | (User.mail == mail))
                if query.count() > 0:
                    self.write(
                        {'success': False, 'message': 'user or email is already exist'})
                else:
                    user = User(username=username,
                                password=password, mail=mail)
                    user.save()
                    self.session.set('user', user)
                    self.write(
                        {'success': True, 'message': 'create user success'})
            except Exception, e:
                self.write({'success': False, 'message': str(e)})
                return


class MainHandler(BaseRequestHandler):

    @gen.coroutine
    def get(self):
        self.redirect('/admin/posts')


class PostListHandler(BaseRequestHandler):

    @login_required
    def get(self):
        self.render('index.html')


class EditPostHandler(BaseRequestHandler):

    @login_required
    def get(self):
        id = self.get_argument('id')
        post = Post.get(id=id)
        self.render('edit.html', title=post.title,
                    content=post.content, id=post.id)


class PostHandler(BaseRequestHandler):

    @login_required
    def get(self):
        self.render('post.html')

    @login_required
    def post(self):
        title = self.get_argument('title')
        content = self.get_argument('content')
        if (not title) or (not content):
            self.write(
                {'success': False, 'message': 'title or conte is not allow empty.'})
        try:
            user_session = self.session.get('user')
            user = User.get(username=user_session.username)
            post = Post.create(title=title, content=content, user=user)
            post.save()
            self.write({'success': True, 'message': 'post success'})
        except Exception, e:
            self.write({'success': False, 'message': str(e)})


class TeamHandler(BaseRequestHandler):

    @login_required
    def get(self):
        self.render('team.html')


class SettingsHandler(BaseRequestHandler):

    @login_required
    def get(self):
        self.render('settings.html')


class TrashHandler(BaseRequestHandler):

    @login_required
    def get(self):
        self.render('trash.html')
