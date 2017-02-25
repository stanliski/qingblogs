#! /usr/bin/env python
# coding: utf-8
from __future__ import print_function

import os
import time

import tornado.ioloop
import tornado.web
import tornado.gen
import tornado.websocket
import tornado.httpserver

import handlers.pages
import handlers.admin.pages
from settings import *

def make_app(**settings):
    settings['template_path'] = 'templates'
    settings['static_path'] = 'static'
    return tornado.web.Application([
        (r'/admin', handlers.admin.pages.MainHandler),
        (r'/admin/post', handlers.admin.pages.PostHandler),
        (r'/admin/team', handlers.admin.pages.TeamHandler),
        (r'/admin/settings', handlers.admin.pages.SettingsHandler),
        (r'/admin/trash', handlers.admin.pages.TrashHandler),
        (r'/admin/login', handlers.admin.pages.LoginHandler),
        (r'/admin/register', handlers.admin.pages.RegisterHandler),
        (r'/admin/find', handlers.admin.pages.FindPasswdHandler),
    ], **settings)

if __name__ == '__main__':
    app = make_app(debug=True)
    http_server = tornado.httpserver.HTTPServer(app, xheaders=True)
    http_server.listen(PORT)
    print('Run server on port {}'.format(PORT))
    tornado.ioloop.IOLoop.current().start()
