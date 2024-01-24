import tornado.web

class Handler(tornado.web.RequestHandler):
    def get(self):
        self.write('<a href="/quote">Please use a valid profile URL</a>')