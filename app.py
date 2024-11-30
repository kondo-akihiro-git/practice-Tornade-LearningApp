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
            1: {"lesson": "Learn Python basics including syntax, variables, and data structures."},
            2: {"lesson": "Learn JavaScript, focusing on functions, arrays, and object-oriented programming."},
            3: {"lesson": "Master Ruby programming, including its syntax, methods, and classes."},
            4: {"lesson": "Java programming for beginners: variables, loops, and object-oriented principles."},
            5: {"lesson": "Learn C++ with a focus on memory management, classes, and templates."},
            6: {"lesson": "Master Go programming, including goroutines, channels, and concurrency."},
            7: {"lesson": "Learn PHP basics, focusing on server-side scripting and web development."},
            8: {"lesson": "Swift for beginners: building iOS apps with UIKit and SwiftUI."},
            9: {"lesson": "Learn C#, including object-oriented principles and .NET framework for web development."},
            10: {"lesson": "Rust programming for systems programming with a focus on memory safety and performance."}
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
