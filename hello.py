## http://flask.pocoo.org/docs/1.0/quickstart/#debug-mode

from flask import Flask

app = Flask(__name__)


@app.route(
    "/"
)  ## We then use the route() decorator to tell Flask what URL should trigger our function.
def hello_world():
    return "Hello, World!"


## The function is given a name which is also used to generate URLs for that particular function,
## and returns the message we want to display in the user’s browser.
