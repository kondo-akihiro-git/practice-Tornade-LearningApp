import tornado.ioloop
import tornado.web

# メインページのハンドラー
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # "/" にアクセスしたときに表示されるコンテンツ
        self.write("Welcome to the Home Page!")

# APIエンドポイント用のハンドラー
class ApiHandler(tornado.web.RequestHandler):
    def prepare(self):
        # CORS設定を追加（フロントエンドとの通信を許可）
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE")
        self.set_header("Access-Control-Allow-Headers", "Content-Type")
    
    def get(self):
        # サンプルデータをJSON形式で返す
        self.write({"message": "Hello from Tornado API!"})

# Aboutページのハンドラー
class AboutHandler(tornado.web.RequestHandler):
    def get(self):
        # "/about" にアクセスしたときに表示されるコンテンツ
        self.write("This is the About Page.")

# Contactページのハンドラー
class ContactHandler(tornado.web.RequestHandler):
    def get(self):
        # "/contact" にアクセスしたときに表示されるコンテンツ
        self.write("Contact us at contact@example.com.")

# アプリケーションのルーティング設定
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),          # メインページ
        (r"/api/data", ApiHandler),   # APIエンドポイント
        (r"/about", AboutHandler),    # Aboutページ
        (r"/contact", ContactHandler) # Contactページ
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Tornado is running at http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()
