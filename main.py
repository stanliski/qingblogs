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
import settings

def make_app(**settings):
    settings['template_path'] = 'template'
    settings['static_path'] = 'static'
    return tornado.web.Application([
        (r'/', handlers.pages.AdminMainHandler),
    ], **settings)


if __name__ == '__main__':
    app = make_app(debug=True)
    http_server = tornado.httpserver.HTTPServer(app, xheaders=True)
    http_server.listen(PORT)
    print('Run server on port {}'.format(PORT))
    tornado.ioloop.IOLoop.current().start()
