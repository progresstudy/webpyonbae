#-*- coding:utf-8 -*-
"""
author: lyz

A simple demo of use webpy
"""
import codecs

import markdown
import web

HTML_HEAD = """<html><head><meta charset="utf-8"></head>
<link href="http://kevinburke.bitbucket.org/markdowncss/markdown.css" rel="stylesheet"></link>
<body>"""
HTML_TAIL = """</body></html>"""

urls = ('/', 'Index')

class Index:
    def GET(self):
        with codecs.open("webpyonbae.md", "r+", encoding="utf-8") as f:
            body = unicode(f.read())
            body = markdown.markdown(body)
        return HTML_HEAD + body + HTML_TAIL
        #return "Hello World"

app = web.application(urls, globals())

"""
def app(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)
    body=["Welcome to Baidu Cloud!\n"]
    return body
"""

from bae.core.wsgi import WSGIApplication
application = WSGIApplication(app.wsgifunc())
