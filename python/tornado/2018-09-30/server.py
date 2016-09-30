import tornado.ioloop
import tornado.web
import socket
import os


class IndexHandler(tornado.web.RequestHandler):
    def get(self):

        self.render("html/index.html",
                    title="home page",
                    header=self.render_string('html/tpl/header.html'),
                    footer='sloba',
                    content='mladen<b>xx</b>'
                    )


def make_app():

    settings = {
        "static_path": os.path.join(os.path.dirname(__file__), "css"),
    }

    return tornado.web.Application([
        (r"/", IndexHandler),
        (r'/css/(main\.css)',
            tornado.web.StaticFileHandler,
            {'path': settings['static_path']}),
    ], debug = socket.gethostname() in ['Igors-Air',])


if __name__ == "__main__":
    app = make_app()
    app.listen(9999)
    tornado.ioloop.IOLoop.current().start()