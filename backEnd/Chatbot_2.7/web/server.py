import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import logging
from logging.handlers import TimedRotatingFileHandler

from chatbot import ChatBot
from flask import Flask, render_template, request


########################################

def init_log(log_file='log/info.log'):

    handler = TimedRotatingFileHandler(log_file, when="D", interval=1, backupCount=7)
    formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')
    handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    return logger

logger = init_log()
bot = ChatBot()
app = Flask(__name__, static_url_path='')

########################################

@app.route('/', methods=['GET', 'POST'])
def view():
    return render_template('index.html')


@app.route('/chat', methods=['GET'])
def response():
    data = request.args.to_dict()
    message = data['message']
    if message != '':
        answer = bot.response(message)
        return answer


@app.route('/forget', methods=['GET'])
def forget():
    bot.forget()
    return 'success'


if __name__ == '__main__':
    print(bot.response('Server started...'))
    app.run('127.0.0.1', debug=True)
