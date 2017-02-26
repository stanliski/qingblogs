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
import handlers.admin
import handlers.api
from settings import *

from tornado.log import enable_pretty_logging

enable_pretty_logging()

def make_app(**settings):
    settings['template_path'] = 'templates'
    settings['static_path'] = 'static'
    settings['cookie_secret'] = 'TODO:_'
    return tornado.web.Application([
        (r'/admin', handlers.admin.MainHandler),
        (r'/admin/post', handlers.admin.PostHandler),
        (r'/admin/team', handlers.admin.TeamHandler),
        (r'/admin/settings', handlers.admin.SettingsHandler),
        (r'/admin/trash', handlers.admin.TrashHandler),
        (r'/admin/login', handlers.admin.LoginHandler),
        (r'/admin/register', handlers.admin.RegisterHandler),
        (r'/admin/find', handlers.admin.FindPasswdHandler),
        # api
        (r'/api/v1/post', handlers.api.ApiPostHandler),
    ], **settings)

if __name__ == '__main__':
    app = make_app(debug=True)
    http_server = tornado.httpserver.HTTPServer(app, xheaders=True)
    http_server.listen(PORT)
    print('Run server on port {}'.format(PORT))
    tornado.ioloop.IOLoop.current().start()
