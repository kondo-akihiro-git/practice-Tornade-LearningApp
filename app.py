import tornado.ioloop
import tornado.web
import os
import json

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header("Content-Type", "application/json")
        self.set_header("Access-Control-Allow-Origin", "*")  # CORSを許可
        categories = [
            {"id": 1, "name": "Python"},
            {"id": 2, "name": "JavaScript"},
            {"id": 3, "name": "Ruby"},
            {"id": 4, "name": "Java"},
            {"id": 5, "name": "C++"},
            {"id": 6, "name": "Go"},
            {"id": 7, "name": "PHP"},
            {"id": 8, "name": "Swift"},
            {"id": 9, "name": "C#"},
            {"id": 10, "name": "Rust"}
        ]
        self.write(json.dumps({"categories": categories}))

class CategoryHandler(tornado.web.RequestHandler):
    def get(self, category_id):
        self.set_header("Access-Control-Allow-Origin", "*")  # CORSを許可
        lessons = {
            1: {"category": "セキュリティ", "keyword": "クラウド", "description": "クラウドとは…"},
            2: {"category": "プログラミング", "keyword": "Python", "description": "Pythonとは…"},
            3: {"category": "プログラミング", "keyword": "JavaScript", "description": "JavaScriptとは…"},
            4: {"category": "データベース", "keyword": "SQL", "description": "SQLとは…"},
            # 他のカテゴリも同様に追加できます
        }
        lesson_data = lessons.get(int(category_id), {"lesson": "No lesson found for this category."})
        self.write(lesson_data)


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
