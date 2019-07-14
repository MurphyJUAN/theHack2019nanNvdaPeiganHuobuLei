import configparser
import shelve
import aiml
import colorama
import wordsegment as ws
import os 
import sys
import string
import json

import tensorflow as tf
import nltk
from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tree import ParentedTree, Tree

from itertools import groupby
from stanfordcorenlp import StanfordCoreNLP

import chatbot.crawler as crawler
import chatbot.deeplearning as deep
import chatbot.kdddatabased as kb
from settings import PROJECT_ROOT
from chatbot.botpredictor import BotPredictor

class ChatBot:
    """
        Intelligent dialogue model based on-
        1. Template-based- AIML
        2. Knowledge Based- MySQL \\\
        3. Web Search
        4. Deep Learning: RNN
    """
    
    # initialize
    colorama.init()
    ws.load()
    #nltk.download()
    
    def __init__(self, config_file='config.cfg', host='http://localhost', port=9000):
        config = configparser.ConfigParser()
        config.read(config_file)
        self.load_file = config.get('resource', 'load_file')
        self.save_file = config.get('resource', 'save_file')
        self.shelve_file = config.get('resource', 'shelve_file')
        self.filter_file = config.get('resource', 'filter_file')
        
        corp_dir = os.path.join(PROJECT_ROOT, 'Data', 'Corpus')
        knbs_dir = os.path.join(PROJECT_ROOT, 'Data', 'KnowledgeBase')
        res_dir = os.path.join(PROJECT_ROOT, 'Data', 'Result')
    
        # Initialize the KERNEL
        self.mybot = aiml.Kernel()
        sess = tf.Session()
        self.predictor = BotPredictor(sess, corpus_dir=corp_dir, knbase_dir=knbs_dir, result_dir=res_dir, result_file='basic')
        self.session_id = self.predictor.session_data.add_session()
        
        # Create AI Engine 
        if os.path.isfile("model\AIChatEngine.brn"):
            self.mybot.bootstrap(brainFile = "model\AIChatEngine.brn")            
        else:
            self.mybot.bootstrap(learnFiles=self.load_file, commands='load aiml b')
            self.mybot.saveBrain("model\AIChatEngine.brn")
            
        # Use an existing server: StanfordCoreNLP
        self.nlp = StanfordCoreNLP(host, port=port, timeout=30000)
        self.props = {
            'annotators': 'tokenize,ssplit,pos,lemma,ner,parse,depparse,dcoref,relation',
            'pipelineLanguage': 'en',
            'outputFormat': 'json'
        }

################################################################
            
    def response(self, user_message):
        # Limit word count
        if len(user_message) > 100:
            return self.mybot.respond('MAX')
        elif len(user_message) == 0:
            return self.mybot.respond('MIN')
        
        # Start chatting
        else:
            #print ('# User original message # > ' + user_message)
            # Word Segmentation: split words e.g. hellohowareyou --> hello how are you
            #segmented_text = ' '.join(ws.segment(user_message))
            #print('# After Segmentation # >'+segmented_text)
            
            # Init Lemmatization 
            wordnet_lemmatizer = WordNetLemmatizer()
            
            # User Sentence Tokenization 
            word_tokens = self.nlp.word_tokenize(user_message)
            
            # Removing stopwords
            stop_words = set(stopwords.words('english')) 
            #stopwords.extend(string.punctuation)
            filtered_sentence = [w for w in word_tokens if not w in stop_words] 
            filtered_stop_words = [] 
            for w in word_tokens: 
                if w not in stop_words: 
                    filtered_stop_words.append(w) 
            
            print(colorama.Fore.RED+'\n------------------ User Input Words --> Lemma -------------------------- '+colorama.Fore.RESET)
            final_sentence = [] 
            for word in filtered_stop_words:
                final_sentence.append(wordnet_lemmatizer.lemmatize(word, pos="v")) 
                print ("{0:10}{1:5}{2:20}".format(word, '--> ', wordnet_lemmatizer.lemmatize(word, pos="v")))
            
            #print(colorama.Fore.GREEN+'\n********************* Dependency Parser ********************* '+colorama.Fore.RESET) 
            #dependency_parser = self.nlp.dependency_parse(' '.join(final_sentence))
            #print(dependency_parser)
            
            # POS Tagger 
            postagger = self.nlp.pos_tag(' '.join(final_sentence))
            print(colorama.Fore.YELLOW+'\n------------------ Identify POS Tagger -------------------------- '+colorama.Fore.RESET)
            print('pos tagger: ', postagger)
            
            print("-----------------------------------------------------------------------")
            grammar = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
            cp = nltk.RegexpParser(grammar)
            #tree = cp.parse(postagger)
            #print ("CP: ", cp)
            tree = cp.parse(postagger)
            print (tree)           
            
            for word, pos in postagger:
                if pos=='NNP':
                    print (word)
            
            
            
            
            print("-----------------------------------------------------------------------")
            #https://github.com/ayat-rashad/ayat-rashad.github.io/blob/master/triples.ipynb
            
            
            # Add all NOUNs into list 
            nounEntityList = [] 
            for pos in postagger:
                if pos[1] in ('NN','NNS','NNP','NNPS'):
                    nounEntityList.append(pos[0])
            print(colorama.Fore.GREEN+'\n------------------ Added NOUN into Entity List ------------------------- '+colorama.Fore.RESET) 
            print(nounEntityList, '\n')                    
            
            botresponse = self.mybot.respond(user_message)
            #print ('# Bot > ' + botresponse)
            
            responseAnswer = '' 
            # Template-based mode
            if botresponse[0] != '#':
                responseAnswer = botresponse
            
            elif botresponse.find('#NONE#') != -1: 
                # KB Searching mode  #
                ######################
                ans = ''
                ans = kb.kdd_search(nounEntityList, ' '.join(final_sentence))
                if ans != '':
                    responseAnswer = ans.encode('utf-8')
                else:
                    # WEB Searching mode #
                    ######################
                    #ans = crawler.web_search(user_message)
                    if ans != '':
                        responseAnswer = ans.encode('utf-8')
                    else:
                        # DEEP Learing- RNN #
                        #####################
                        ans = deep.neural_network(self, user_message)
                        responseAnswer = ans.encode('utf-8')
            
            # Self-Learning Mode
            elif botresponse.find('#LEARN#') != -1:
                print ('Learning Mode--> ' +botresponse)
                question = botresponse[8:]
                answer = user_message
                self.save(question, answer)
                responseAnswer = self.mybot.respond('Already studied')
                
            # check for BUG
            else:
                responseAnswer = self.mybot.respond('I don\'t know.')
            
            return responseAnswer 

    def save(self, question, answer):
        db = shelve.open(self.shelve_file, 'c', writeback=True)
        db[question] = answer
        db.sync()
        rules = []
        for r in db:
            rules.append(self.category_template.format(pattern=r, answer=db[r]))
        with open(self.save_file, 'w') as fp:
            fp.write(self.template.format(rule='\n'.join(rules)))

    def forget(self):
        os.remove(self.save_file) if os.path.exists(self.save_file) else None
        os.remove(self.shelve_file) if os.path.exists(self.shelve_file) else None
        self.mybot.bootstrap(learnFiles=self.load_file, commands='load aiml b')
        
    def find_subject(t):
        print("************* find me*******************")
        for s in t.subtrees(lambda t: t.label() == 'NP'):
            for n in s.subtrees(lambda n: n.label().startswith('NN')):                
                return (n[0], self.find_attrs(n))
    
    def find_predicate(t):    
        v = None
        for s in t.subtrees(lambda t: t.label() == 'VP'):
            for n in s.subtrees(lambda n: n.label().startswith('VB')):
                v = n
            return (v[0], self.find_attrs(v))
    
    def find_object(t):    
        for s in t.subtrees(lambda t: t.label() == 'VP'):
            for n in s.subtrees(lambda n: n.label() in ['NP', 'PP', 'ADJP']):
                if n.label() in ['NP', 'PP']:
                    for c in n.subtrees(lambda c: c.label().startswith('NN')):
                        return (c[0], self.find_attrs(c))
                else:
                    for c in n.subtrees(lambda c: c.label().startswith('JJ')):
                        return (c[0], self.find_attrs(c))
                
    def find_attrs(node):
        attrs = []
        p = node.parent()
        
        # Search siblings
        if node.label().startswith('JJ'):
            for s in p:
                if s.label() == 'RB':
                    attrs.append(s[0])                
        elif node.label().startswith('NN'):
            for s in p:
                if s.label() in ['DT','PRP$','POS','JJ','CD','ADJP','QP','NP']:
                    attrs.append(' '.join(s.flatten()))
        elif node.label().startswith('VB'):
            for s in p:
                if s.label() == 'ADVP':
                    attrs.append(' '.join(s.flatten()))
                    
        # Search uncles
        if node.label().startswith('JJ') or node.label().startswith('NN'):
            for s in p.parent():
                if s != p and s.label() == 'PP':
                    attrs.append(' '.join(s.flatten()))
        elif node.label().startswith('VB'):
            for s in p.parent():
                if s != p and s.label().startswith('VB'):
                    attrs.append(s[0])
        return attrs

if __name__ == '__main__':
    bot = ChatBot()
    while True:		
        user_message = raw_input('User > ')
        print ('Bot > ' + bot.response(user_message))
