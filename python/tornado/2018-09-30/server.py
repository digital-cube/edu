import tornado.ioloop
import tornado.template
import tornado.web
import socket
import json
import os


class IndexHandler(tornado.web.RequestHandler):
    def get(self):

        self.render("html/index.html",
                    title="home page",
                    )


class NewsHandler(tornado.web.RequestHandler):
    def get(self):

        news = json.load(open('news/index.json'))
        for item in news:
            if 'html-content' in item:
                with open('news/'+item['html-content'], 'r') as f:
                    item['content'] = f.read()

        self.render("html/news.html",
                    title="news page",
                    news=news
                    )


class NewsModule(tornado.web.UIModule):
    def render(self, news):
        return self.render_string('modules/news.html', news=news)


def make_app():

    settings = {
        "static_path": os.path.join(os.path.dirname(__file__), "css"),
        "ui_modules": {"News": NewsModule},
    }

    return tornado.web.Application([
                (r"/", IndexHandler),
                (r"/news", NewsHandler),
                (r'/css/(main\.css)', tornado.web.StaticFileHandler, {'path': settings['static_path']}),
                ],
            debug=socket.gethostname() in ['Igors-Air',], **settings)


if __name__ == "__main__":
    app = make_app()
    app.listen(9999)
    tornado.ioloop.IOLoop.current().start()