import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):

    def get(self):

        with open('index.html') as f:
            content = f.read()

        self.write(content)


class TemplateHandler(tornado.web.RequestHandler):

    def get(self):

        self.render("index-tpl.html",
                    title="My title",
                    items=["Item 1", "Item 2", "Item 3", "Item 4","Item 4","Item 4","Item 4","Item 4"])


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/template", TemplateHandler),
    ], debug=True)


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
