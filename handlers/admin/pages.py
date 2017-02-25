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
        username = self.get_argument('username', None)
        password = self.get_argument('passwd', None)
        if (not username) or (not password):
            self.write({'success': False, 'message': "username or passwd is not allowed to be empty"})
        else:
            try:
                user = models.User.select().where(models.User.username == username).get()
                if user is not None and user.verify_password(password):
                    self.write({'success': True, 'message': user.to_json()})
                else:
                    self.write({'success': False, 'message': 'user password is not right'})
            except Exception, e:
                self.write({'success': False, 'message': str(e)})

class RegisterHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('admin/account/register.html')

    def post(self):
        username = self.get_argument('username', None)
        passwd = self.get_argument('passwd', None)
        mail = self.get_argument('mail', None)
        if (not username) and (not passwd) and (not mail):
            self.redirect('/admin')
        else:
            self.write({'success': False})

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
