# coding: utf-8
import tornado.web
from tornado import gen

from models import *
import peewee
from peewee import fn
from peewee import RawQuery
from .common import BaseRequestHandler


class FindPasswdHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('admin/account/forgetpasswd.html')


class LoginHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('admin/account/login.html')

    def post(self):
        username = self.get_argument('username', None)
        password = self.get_argument('password', None)
        if (not username) or (not password):
            self.write(
                {'success': False, 'message': "username or passwd is not allowed to be empty"})
            return
        try:
            user = User.get((User.username == username)
                            | (User.mail == username))
        except Exception, e:
            self.write({'success': False, 'message': 'user is not exist'})
            return
        if user.verify_password(password):
            self.write({'success': True, 'message': 'login success'})
        else:
            self.write({'success': False, 'message': 'password is not right'})


class LogoutHandler(tornado.web.RequestHandler):

    def get(self):
        self.session.set('user', None)
        self.redirect('')
        return


class RegisterHandler(tornado.web.RequestHandler):

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
                user = models.User.create(
                    username=username, password=password, mail=mail)
                user.save()
                self.write({'success': True, 'message': 'create user success'})
            except Exception, e:
                self.write({'success': False, 'message': str(e)})
                return


class MainHandler(BaseRequestHandler):

    @gen.coroutine
    def get(self):
        self.render('index.html')


class PostHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('post.html')

    def post(self):
        title = self.get_argument('title')
        content = self.get_argument('content')
        if (not title) or (not content):
            self.write(
                {'success': False, 'message': 'title or conte is not allow empty.'})
        try:
            user = User.get(username='stanley')
            post = Post.create(title=title, content=content, user=user)
            post.save()
            self.write({'success': True, 'message': 'post success'})
        except Exception, e:
            self.write({'success': False, 'message': str(e)})


class TeamHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('team.html')


class SettingsHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('settings.html')


class TrashHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('trash.html')
