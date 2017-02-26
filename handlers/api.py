# coding: utf-8

import json
import urlparse

import tornado.websocket
from tornado import escape
from tornado import gen
from models import *
from .common import BaseRequestHandler

class ApiPostHandler(BaseRequestHandler):

    def get(self):
        try:
            posts = Post.select()
            json_post = []
            for post in posts:
                json_post.append(post.to_json())
            self.write_json({
                "success": True,
                "posts": json_post,
            })
            return
        except Exception, e:
            return

    def post(self):
        print 'post'

    def put(self):
        print 'put'

    def delete(self):
        print 'delete'
