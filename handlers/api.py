# coding: utf-8

import json
import urlparse

import tornado.websocket
from tornado import escape
from tornado import gen
from models import Post
from .common import BaseRequestHandler


class ApiTagHandler(BaseRequestHandler):

    def get(self):
        print 'get'

    def post(self):
        print 'post'

    def put(self):
        print 'put'

    def delete(self):
        print 'delete'


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
            self.write_json({
                'sucess': False,
                'message': str(e)
            })
            return

    def post(self):
        print 'post'

    def put(self):
        print 'put'

    def delete(self):
        id = self.get_argument('id', None)
        try:
            post = Post.get(id=id)
            post.delete_instance()
            self.write_json({'success': True})
        except Exception, e:
            self.write_json({'success': False, 'message': str(e)})
