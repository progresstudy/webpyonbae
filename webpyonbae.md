##如何在BAE通过web.py制作网站

####1. 添加依赖

	touch requirements.txt
	cat <<EOF > requirements.txt
	markdown
	jinja2
	EOF
	#注web.py 模块无法通过添加依赖方式自动安装，发布时报错
	#故采用一下方法补救

####2. 下载web.py库
	wget https://github.com/webpy/webpy/archive/master.zip
		
	
####3. 拷贝库到bae实例库根目录下
	unzip master.zip -d webpy
	cp -r webpy/web path/to/you/bae

	
####3. 修改index.py

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
    
####4. 添加模板
	mkdir templates
	touch templates/demo.html
	cat <<EOF > templates/demo.html
    <html>
      <head>
        <meta charset="utf-8">
        <link href="http://kevinburke.bitbucket.org/markdowncss/markdown.css" rel="stylesheet">
        </link>
      </head>
      <body>
        {{ html_body }}
      </body>
    </html>
    EOF

####5. 添加md文档
由于是demo，仅简单的处理了一个请求，和一个md文档：webpyonbae.md

可以根据webpy使用方法和markdown使用方法添加更多想要的功能
  
####6. 提交代码

	git add .
	git commit -m "first commit"
	git push origin master

####7. 重新快速部署

------

**demo代码:** [git webpy demo](https://github.com/progresstudy/webpyonbae)