# coding: utf-8
import tornado.web
import tornado

class AdminMainHandler (tornado.web.RequestHandler):

    def get(self):
        self.render('index.html')


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('index.html')
