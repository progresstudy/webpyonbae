##如何在BAE通过webpy制作网站

####1. 下载webpy库
	wget https://github.com/webpy/webpy/archive/master.zip
	
####2. 下载markdown库

	wget https://pypi.python.org/packages/source/M/Markdown/Markdown-2.4.1.zip
	
	
####2. 拷贝库到bae实例库根目录下
	unzip master.zip -d webpy
	cp -r webpy/web path/to/you/bae
	unzip Markdown-2.4.1.zip -d markdown
	cp -r markdown/Markdown-2.4.1/markdown /path/to/you/bae
	
####3. 修改index.py

    #-*- coding:utf-8 -*-
    """
    author: lyz

    A simple demo of use webpy
    """
    import codecs

    import markdown
    import web

    HTML_HEAD = """<html><head><meta charset="utf-8"></head><body>
    <link href="http://kevinburke.bitbucket.org/markdowncss/markdown.css" rel="stylesheet"></link>"""
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
####4. 提交代码

	git add .
	git commit -m "first commit"
	git push origin master

####5. 重新快速部署

------

**demo代码:** [git webpy demo](https://github.com/progresstudy/webpyonbae)