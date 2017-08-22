#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web


count = 0

class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        global count
        count += 1
        self.write("Hello, vicky! %s" % count)


