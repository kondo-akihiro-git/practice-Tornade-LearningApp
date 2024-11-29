import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, Tornado!")

class ApiHandler(tornado.web.RequestHandler):
    def prepare(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE")
        self.set_header("Access-Control-Allow-Headers", "Content-Type")
    
    def get(self):
        self.write({"message": "Hello from Tornado!"})

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/api/data", ApiHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Tornado is running at http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()
