from flask import Flask

app = Flask(__name__)

from js_example import views

''' Project layout:

Fileserver/
    config.py
    requirements.txt
    run.py
    setup.py
    app/
        __init__.py
        static/
            css/
            img/
            js/
        templates/
            formAction.html
            formSubmit.html
            index.html '''