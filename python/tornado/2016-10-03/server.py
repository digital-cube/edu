import tornado.ioloop
import tornado.web
import json
import os

class ContactHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('html/contact.html')
    
    
    
class MainHandler(tornado.web.RequestHandler):
    def get(self):

        with open('products.json', 'r') as f:
            products = json.load(f)

        nr=0
        for product in products:
            nr += 1
            if 'image-pos' not in product:
                product['image-pos'] = 'pull-left' if nr%2==1 else 'pull-right'

            if 'bg-color' not in product:

                product['bg-color'] = 'gray' if nr%2==0 else 'white'

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
        "static_path_pages": os.path.join(os.path.dirname(__file__), "css"),
        "static_path_inc": os.path.join(os.path.dirname(__file__), "css"),
        "static_path_img": os.path.join(os.path.dirname(__file__), "images"),
    }

    return tornado.web.Application([
        (r"/",MainHandler),
        (r"/contact/?", ContactHandler),
        (r'/css/(.*)', tornado.web.StaticFileHandler, {'path': settings['static_path']}),
        (r'/css/pages/(.*)', tornado.web.StaticFileHandler, {'path': settings['static_path_pages']}),
        (r'/css/inc/(.*)', tornado.web.StaticFileHandler, {'path': settings['static_path_inc']}),
        (r'/images/(.*)', tornado.web.StaticFileHandler, {'path': settings['static_path_img']}),

    ], debug=True, **settings)


if __name__ == "__main__":
    app = make_app()
    app.listen(1122)
    tornado.ioloop.IOLoop.current().start()