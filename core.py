#! /usr/bin/env python
import functools

def login_required2(f):
    @functools.wraps(f)
    def inner(*args, **kwargs):
        request_handler = args[0]
        if not request_handler.current_user:
            return request_handler.write(u'未登录！')
        return f(*args, **kwargs)
    return inner
