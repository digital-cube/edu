import tornado.ioloop
import tornado.web
import json
import os


class MainHandler(tornado.web.RequestHandler):
    def get(self):

        with open('products.json', 'r') as f:
            products = json.load(f)

        for product in products:
            if 'image-pos' not in product:
                product['image-pos'] = 'left'

            if 'content' not in product:
                if 'content-file' not in product:
                    product['content'] = 'missing content'
                else:
                    try:
                        with open('html/'+product['content-file'],'r') as f:
                            product['content'] = f.read()
                    except Exception as e:
                        product['content'] = 'error reading content from file {}'.format(product['content-file'])


        self.render("html/products.html", products=products)


def make_app():

    settings = {
        "static_path": os.path.join(os.path.dirname(__file__), "css"),
    }

    return tornado.web.Application([
        (r"/", MainHandler),
        (r'/css/(.*)', tornado.web.StaticFileHandler, {'path': settings['static_path']}),
    ], debug=True, **settings)


if __name__ == "__main__":
    app = make_app()
    app.listen(1122)
    tornado.ioloop.IOLoop.current().start()