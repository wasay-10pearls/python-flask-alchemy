from flask import Flask, request
import middleware

app = Flask(__name__)

app.wsgi_app = middleware.Middleware(app.wsgi_app)

@app.route('/', methods=['GET', 'POST'])
def hello():
    # using 
    user = request.environ['user']
    return "Hi %s"%user['name']

if __name__ == "__main__":
    app.run()