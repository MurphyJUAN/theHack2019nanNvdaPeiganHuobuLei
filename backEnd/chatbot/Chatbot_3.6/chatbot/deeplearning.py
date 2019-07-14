import os
import sys
import json
import requests
import tensorflow as tf
import colorama
from bs4 import BeautifulSoup
from settings import PROJECT_ROOT
from chatbot.botpredictor import BotPredictor

colorama.init()

# Turing robot
def neural_network(self, message):
    
    ans_response = ''
    ans_response = self.predictor.predict(self.session_id, message)
    print(ans_response) 
    
    return ans_response


if __name__ == '__main__':
    print (rnn_generator('AI Chatbot')) 
