# coding: utf-8
import tornado.web
import tornado
import models

class FindPasswdHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('admin/account/forgetpasswd.html')

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('admin/account/login.html')

    def post(self):
        print 'post'

class RegisterHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('admin/account/register.html')

    def post(self):
        print 'post'

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('admin/index.html')

class PostHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('admin/post.html')

    def post(self):
        title = self.get_argument('title');
        content = self.get_argument('content');
        if (not title) or (not content):
            self.write({'success': False, 'description': 'title or conte is not allow empty.'})
        self.write({'success': True})

class TeamHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('admin/team.html')

class SettingsHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('admin/settings.html')

class TrashHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('admin/trash.html')
