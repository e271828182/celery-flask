# -*- coding=utf-8 -*-
from webapp import create_app


flask_app = create_app()


if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', port=8888, debug=True)
