import tornado.ioloop
import tornado.web
import os

# ハンドラークラスを作成
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", message="Welcome to the Learning Site!")

class LessonHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("lesson.html", lesson_title="Lesson 1: Introduction to Python")

class AboutHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("about.html", message="This is the About Page")

class ContactHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("contact.html", message="Contact Us Here")


# Tornadoの設定
def make_app():
    return tornado.web.Application(
        [
            (r"/", MainHandler),
            (r"/lesson", LessonHandler),
            (r"/about", AboutHandler),
            (r"/contact", ContactHandler),
        ],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
    )


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)  # ポート8888でアプリケーションを実行
    tornado.ioloop.IOLoop.current().start()  # Tornadoの非同期ループを開始
