# coding: utf-8

import os
import sys
reload(sys)
sys.setdefaultencoding('gb18030')

PORT = int(os.environ.get("PORT", 5000))
SQLITE_URL = os.environ.get("SQLITE_URL", 'post.db')
