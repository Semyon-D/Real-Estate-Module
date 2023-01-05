import logging

class LoggingMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        # Log the request
        logging.info(f'Request: {environ["REQUEST_METHOD"]} {environ["PATH_INFO"]}')

        # Call the next middleware or the application
        return self.app(environ, start_response)

#To use this middleware, you will need to wrap your API in the middleware and pass the API as an argument to the middleware.
# Here is an example of how to do this using the Flask web framework:



from flask import Flask
from logging_middleware import LoggingMiddleware

app = Flask(__name__)
app.wsgi_app = LoggingMiddleware(app.wsgi_app)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
