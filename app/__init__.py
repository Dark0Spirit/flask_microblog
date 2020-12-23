from flask import Flask

app = Flask(__name__)


def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()


# 从app包中导入模块routes
from app import routes
