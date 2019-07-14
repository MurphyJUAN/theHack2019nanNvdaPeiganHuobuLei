#coding=utf-8

from flask import Flask, request
#from werkzeug.contrib.fixers import ProxyFix
import checkGrammar as cg
import json

app = Flask(__name__)

# Use the fixer
#app.wsgi_app = ProxyFix(app.wsgi_app)

#=====require=====

#=====error======

#=====func=====
@app.route('/test', methods=['POST', 'GET'])
def url_parameters():
    a = request.args.get("username")
    return a

@app.route('/', methods=['POST', 'GET'])
def helloworld():
    code = json.dumps([{'code': '1'}])
    return code

@app.route('/username', methods=['POST'])
def post_parameter():
    return request.form['username']

@app.route('/checkGrammar', methods=['POST'])
def checkGrammar():
    text = request.json['text']
    if not text:
        return cg.checkGrammar(text)
    else:
        return json.dumps([{'code': '1'}])
    
    

#=====Main=====
if __name__ == '__main__':
    app.run(host='0.0.0.0')
    #app.run()
