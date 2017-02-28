#! /usr/bin/env python
import functools
import redis
from pycket.session import SessionMixin


def login_required(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        self = args[0]
        user = self.session.get('user')
        if not user:
            return self.redirect('/admin/login')
        return f(*args, **kwargs)
    return wrapper
