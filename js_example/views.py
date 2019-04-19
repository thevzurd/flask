from flask import jsonify, render_template, request, url_for

from js_example import app
from js_example import converter as cv
import random
import json

@app.route('/')
def home():
##    main("", "")
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
def main(inp, out):
    bases = ['A', 'C', 'U', 'G']
    if not inp:
        l = random.randint(10, 20)
        inp = [random.choice(bases) for _ in range(l)]

    if not out:
        l = random.randint(10, 20)
        out = [random.choice(bases) for _ in range(l)]

    _, seq, constrain, conv_output, fold1, fold2, ed1, ed2, mfe1, mfe2 = \
        cv.convgen(inp, out)

    data = {}
    data['Sequence'] = seq
    data['Inactive'] = fold1
    data['Inactive MFE'] = mfe1
    data['Inactive ED'] = ed1
    data['Active'] = fold2
    data['Active MFE'] = mfe2
    data['Active ED'] = ed2
    data['Input'] = "".join(inp)
    data['Output'] = "".join(out)

    with open('output.json', 'w') as f:
        json.dump(data, f)

    print('>1')
    print(seq)
    print(fold1)
    print('>2')
    print(seq)
    print(fold2)