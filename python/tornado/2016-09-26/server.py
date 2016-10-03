'''
http://www.tornadoweb.org

sudo pip3.5 install tornado

-- tuple


ADRESA:
http://api.example.com/users

GET - get users ::  GET http://api.example.com/users
   [ [ u00000123, pera ], [ u00000124, zika ] ]

POST - xxx

PUT - put users ::  PUT http://api.example.com/users?username=laza

GET - get users ::  GET http://api.example.com/users
   [ [ u00000123, pera ], [ u00000124, zika ], [ u00000912, laza] ]

PATCH http://api.example.com/users/u00000124/?username=Zika

DELETE http://api.example.com/users/u00000912


'''

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('''
<head>
  <title>Demo APP</title>
</head>
<body>
<p>Hello World ...</p>
<a href="/about">Click here for about page</a>
</body>
        ''')


class AboutHandler(tornado.web.RequestHandler):
    def post(self):
        self.write("About me kroz POST")
    def get(self):
        self.write('''
<head>
  <title>Demo APP</title>
</head>
<body>
<p>About me</p>
<a href="/">home</a>
</body>
        ''')


    def patch(self):
        self.write("About me kroz PATCH")

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", MainHandler),
        (r"/about", AboutHandler),
    ], debug=True)

    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
