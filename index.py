#-*- coding:utf-8 -*-
"""
author: lyz

A simple demo of use webpy
"""
import codecs

import markdown
import web
from web.contrib.template import render_jinja

urls = ('/', 'Index')
### Templates
render = render_jinja('templates',
             encoding = 'utf-8')

class Index:
    def GET(self):
        with codecs.open("webpyonbae.md", "r+", encoding="utf-8") as f:
            body = unicode(f.read())
            body = markdown.markdown(body)
        return render.demo({"html_body": body})
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
