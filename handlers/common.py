# coding: utf-8
import json
import redis
import tornado.web
from tornado import gen
from pycket.session import SessionMixin


class BaseRequestHandler(tornado.web.RequestHandler, SessionMixin):

    def _date_handler(self, obj):
        return obj.isoformat() if hasattr(obj, 'isoformat') else obj

    def write_json(self, data):
        """
        Support datetime json dumps
        """
        self.set_header('Content-Type', 'application/json; charset=utf-8')
        self.write(json.dumps(data, default=self._date_handler))

    def write_image(self, data):
        """
        Support image response
        """
        self.set_header("Content-type",  "image/png")
        self.write(data)
