import tornado.ioloop
import tornado.web
import os
import json

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header("Content-Type", "application/json")
        self.set_header("Access-Control-Allow-Origin", "*")  # CORSを許可
        categories = [
            {"id": 1, "name": "セキュリティ"},
            {"id": 2, "name": "プログラミング"},
            {"id": 3, "name": "フロントエンド"},
            {"id": 4, "name": "データベース"},
        ]
        self.write(json.dumps({"categories": categories}))

class CategoryHandler(tornado.web.RequestHandler):
    def get(self, category_id):
        self.set_header("Access-Control-Allow-Origin", "*")  # CORSを許可
        data = {
            1: [
                {"category": "セキュリティ", "keyword": "クラウド", "description": "クラウドとは…"},
                {"category": "セキュリティ", "keyword": "Adobe", "description": "Adobeとは…"}
            ],
            2: [
                {"category": "プログラミング", "keyword": "Python", "description": "Pythonとは…"}
            ],
            3: [
                {"category": "フロントエンド", "keyword": "JavaScript", "description": "JavaScriptとは…"},
                {"category": "フロントエンド", "keyword": "TypeScript", "description": "TypeScriptとは…"}
            ],
            4: [
                {"category": "データベース", "keyword": "SQL", "description": "SQLとは…"}
            ]
        }
        category_data = data.get(int(category_id), [])
        self.write({"lessons": category_data})



def make_app():
    return tornado.web.Application([
        (r"/dashboard", MainHandler),
        (r"/category/(\d+)", CategoryHandler),  # ID付きのエンドポイント
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)  # ポート8888で実行
    print("API実行 start")
    tornado.ioloop.IOLoop.current().start()
