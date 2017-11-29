# -*- coding: utf-8 -*-
from tornado import web, httpserver, ioloop


class IndexPageHandler(web.RequestHandler):
        def data_received(self, chunk):
            pass

        def get(self):
            self.write("Hello, world")

application = web.Application([
    (r"/", IndexPageHandler),
])

if __name__ == '__main__':
    http_server = httpserver.HTTPServer(application)
    http_server.listen(8080)
    ioloop.IOLoop.current().start()