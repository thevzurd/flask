from flask import jsonify, render_template, request, url_for

from js_example import app

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/output')
def output():
    return render_template('output.html')

''' @app.route('/', defaults={'js': 'plain'})
@app.route('/<any(plain, jquery, fetch):js>')
def index(js):
    return render_template('{0}.html'.format(js), js=js) '''
''' 

@app.route('/add', methods=['POST'])
def add():
    a = request.form.get('a', 0, type=float)
    b = request.form.get('b', 0, type=float)
    return jsonify(result=a + b) '''
