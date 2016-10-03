import tornado.ioloop
import tornado.web
import os

class IndexHandler(tornado.web.RequestHandler):

    def get(self):

        self.render("html/index.html",
                    title="My title",
                    header=self.render_string('html/templates/header.html'),
                    content=self.render_string('html/templates/news.html'),
                    footer=self.render_string('html/templates/footer.html'))


def make_app():

    settings = {
        "static_path": os.path.join(os.path.dirname(__file__), "sass"),
    }

    return tornado.web.Application([
        (r"/", IndexHandler),
        (r'/(main\.css)', tornado.web.StaticFileHandler, {'path': settings['static_path']})

    ], dict(static_path=settings['static_path']), debug=True)


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
