#coding=utf-8

from flask import Flask, request
#from werkzeug.contrib.fixers import ProxyFix
import checkGrammar as cg
import analyzeParagraph as ap
import json


app = Flask(__name__)

# Use the fixer
#app.wsgi_app = ProxyFix(app.wsgi_app)

#=====require=====

#=====error======

#=====func=====
@app.route('/test', methods=['POST'])
def url_parameters():
    a = request.args.get("username")
    return a

@app.route('/', methods=['POST'])
def helloworld():
    code = json.dumps([{'page': 'homepage', 'code': '-3'}])
    return code

@app.route('/username', methods=['POST'])
def post_parameter():
    return request.form['username']

@app.route('/checkGrammar', methods=['POST'])
def checkGrammar():
    text = request.json['text']
    if text:
        ret = cg.checkGrammar(text)
        return ret
    else:
        return json.dumps([{'code': '1'}])

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.json['text']
    try:
        if text:
            ret = ap.analyze(text)
            return ret
        else:
            return json.dumps([{'chose_para': 'None', 'chose_url': 'None'}])
    except:
        return json.dumps([{'chose_para': 'None', 'chose_url': 'None'}])
    
    

#=====Main=====
if __name__ == '__main__':
    #print(ap.analyze('I like swimming'))
    app.run(host='0.0.0.0')
    #app.run() #localhost
