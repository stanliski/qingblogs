# coding: utf-8
import json
import tornado.web
from tornado import gen


class BaseRequestHandler(tornado.web.RequestHandler):

    def _date_handler(self, obj):
        return obj.isoformat() if hasattr(obj, 'isoformat') else obj

    def write_json(self, data):
        """
        Support datetime json dumps
        """
        self.set_header('Content-Type', 'application/json; charset=utf-8')
        self.write(json.dumps(data, default=self._date_handler))
