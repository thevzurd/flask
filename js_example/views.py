from flask import jsonify, render_template, request, url_for, make_response, redirect
# https://stackoverflow.com/questions/42406516/python-flask-render-template-html-did-not-render-correctly
# https://stackoverflow.com/questions/48015074/flask-render-template-doesnt-work-on-ajax-post
from js_example import app
from js_example import converter as cv
import random
import json
import time

def main(inp, out):
    bases = ['A', 'C', 'U', 'G']
    if not inp:
        l = random.randint(10, 20)
        inp = [random.choice(bases) for _ in range(l)]

    if not out:
        l = random.randint(10, 20)
        out = [random.choice(bases) for _ in range(l)]

    outputFileName = "J" + str(int(time.time()))

    cv.convgen(inp, out, outputFileName)

    return jsonify({'status': 'success', 'jobID': outputFileName})


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/input', methods=['POST'])
def input():
    inp = request.form.get('inpSequence', '', type=str)
    out = request.form.get('outSequence', '', type=str)
    return main(inp, out)


@app.route('/output/<jobId>')
def output(jobId):
    with open(jobId + '.output', 'r') as f:
        try:
            fl =f.readlines()
            sequence = fl[0].replace('\n','')
            inactive = fl[1].replace('\n','')
            inactiveMFE = fl[2].replace('\n','')
            inactiveED = fl[3].replace('\n','')
            active = fl[4].replace('\n','')
            activeMFE = fl[5].replace('\n','')
            activeED = fl[6].replace('\n','')
            inputSeq =  fl[7].replace('\n','')
            outputSeq = fl[8].replace('\n','')
            f.close()
            return render_template('output.html', sequence=sequence, inactive=inactive,inactiveMFE=inactiveMFE,inactiveED=inactiveED,active=active,activeMFE=activeMFE,activeED=activeED,inputSeq=inputSeq,outputSeq=outputSeq)
        except:
            return 404