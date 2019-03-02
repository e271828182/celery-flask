from webapp import create_app
flask_app = create_app()


from webapp import make_celery
celery = make_celery(flask_app)


if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', debug=True)
