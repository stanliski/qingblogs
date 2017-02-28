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
    settings['pycket'] = {
        'engine': 'redis',
        'storage': {
            'host': 'localhost',
            'port': 6379,
            'db_sessions': 10,
            'db_notifications': 11,
            'max_connections': 2**31,
        },
        'cookies': {
            # 5 设置过期时间
            'expires_days': 2,
        },
    }
    return tornado.web.Application([
        (r'/admin', handlers.admin.MainHandler),
        (r'/admin/post', handlers.admin.PostHandler),
        (r'/admin/team', handlers.admin.TeamHandler),
        (r'/admin/settings', handlers.admin.SettingsHandler),
        (r'/admin/trash', handlers.admin.TrashHandler),
        (r'/admin/login', handlers.admin.LoginHandler),
        (r'/admin/logout', handlers.admin.LogoutHandler),
        (r'/admin/register', handlers.admin.RegisterHandler),
        (r'/admin/find', handlers.admin.FindPasswdHandler),
        (r'/admin/posts', handlers.admin.PostListHandler),
        (r'/admin/edit', handlers.admin.EditPostHandler),
        # api
        (r'/api/v1/post', handlers.api.ApiPostHandler),
    ], **settings)

if __name__ == '__main__':
    app = make_app(debug=True)
    http_server = tornado.httpserver.HTTPServer(app, xheaders=True)
    http_server.listen(PORT)
    print('Run server on port {}'.format(PORT))
    tornado.ioloop.IOLoop.current().start()
