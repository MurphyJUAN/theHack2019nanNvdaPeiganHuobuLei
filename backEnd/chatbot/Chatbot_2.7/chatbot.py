import configparser
import shelve
import aiml
import wordsegment as ws
import os 
import crawler
import deeplearning
import knowledgebased as kb
import mysql.connector


class ChatBot:
    """
        Intelligent dialogue model based on-
        1. Template-based- AIML 
        2. Knowledge Based- MySQL  
        3. Web Search 
        4. Deep Learning: RNN 
    """
    
    def __init__(self, config_file='config.cfg'):
        config = configparser.ConfigParser()
        config.read(config_file)
        self.load_file = config.get('resource', 'load_file')
        self.save_file = config.get('resource', 'save_file')
        self.shelve_file = config.get('resource', 'shelve_file')
        self.filter_file = config.get('resource', 'filter_file')

        # initialize
        ws.load()
        
        # Initialize the KERNEL 
        self.mybot = aiml.Kernel()
        
        # Create AI Engine 
        if os.path.isfile("AIChatEngine.brn"):
            # if exist, Need to overwrite the AIEngine 
            self.mybot.bootstrap(brainFile = "AIChatEngine.brn")
        else:
            self.mybot.bootstrap(learnFiles=self.load_file, commands='load aiml b')
            self.mybot.saveBrain("AIChatEngine.brn")            

    def response(self, message):
        # Limit word count
        if len(message) > 100:
            return self.mybot.respond('MAX')
        elif len(message) == 0:
            return self.mybot.respond('MIN')    
        
        # End chat
        if message == 'exit' or message == 'quit':
            return self.mybot.respond('Thank you for using Chatbot. Good Bye')         
        
        # Start chatting
        else:
            userAsk = self.mybot.respond(' '.join(ws.segment(message)))
            
            # Template-based mode
            if userAsk[0] != '#':
                print ('Template-based mode--> ' + userAsk)
                return userAsk
            
            elif userAsk.find('#NONE#') != -1:
                # KB Searching mode  #
                ######################
                print ('Database Searching mode--> ' + userAsk)
                ans = ''
                ans = kb.knowledge_search(message)
                print (ans)
                if ans != '':
                    return ans.encode('utf-8')
                else:
                    # WEB Searching mode #
                    ######################
                    print ('Web Searching mode--> ' + userAsk)
                    ans = crawler.search(message)
                    if ans != '':
                        return ans.encode('utf-8')
                        print (ans)
                    else:
                        # DEEP Learing- RNN #
                        #####################
                        print ('Neural Network mode--> ' + userAsk)
                        ans = deeplearning.rnn_generator(message)
                        return ans.encode('utf-8')
            
            # Self-Learning Mode
            elif userAsk.find('#LEARN#') != -1:
                print ('Learning Mode--> ' +userAsk)
                question = userAsk[8:]
                answer = message
                self.save(question, answer)
                return self.mybot.respond('Already studied')
                
            # check for BUG
            else:
                return self.mybot.respond('I don\'t know.')

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


if __name__ == '__main__':
    bot = ChatBot()	
    while True:		
        message = raw_input('User > ')
        print ('Bot > ' + bot.response(message))
