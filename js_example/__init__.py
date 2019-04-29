# https://medium.freecodecamp.org/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492
# https://stackoverflow.com/questions/18713086/virtualenv-wont-activate-on-windows

##from flask_scss import Scss
from flask import Flask

app = Flask(__name__)

##Scss(app, static_dir='static', asset_dir='assets')

from js_example import views
if __name__ == "__main__":
    app.run(debug=True)
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