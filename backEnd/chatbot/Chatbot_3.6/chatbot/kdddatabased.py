import mysql.connector
import collections
import colorama
import string
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords 
from nltk.stem import WordNetLemmatizer

colorama.init()
wordnet_lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english')) 

# Knowledge-based (KDD)Search
def kdd_search(nounEntityList, user_input_text):     
    
    try:
        # Connect to MySQL Database 
        connection = mysql.connector.connect(host='localhost',
                                 database='aichatbot',
                                 user='root',
                                 password='')
                                 
        if connection.is_connected():
           db_Info = connection.get_server_info()
           #print("Connected to MySQL database... MySQL Server version on ",db_Info)
           dbcursor = connection.cursor()
           #dbcursor.execute("select database();")
           #record = dbcursor.fetchone()
           #print ("Your connected to - ", record)
           
           queryResultList=[]
           row_count=0
           for entity in nounEntityList:
               mysqlstatement = 'SELECT id, response_count, tag_id, question, response_message, keywords, message_type FROM knowledgebase WHERE question like\'%'+entity+'%\' OR keywords like\'%'+entity+'%\' OR response_message like\'%'+entity+'%\'  '
               dbcursor.execute(mysqlstatement)
               qres = dbcursor.fetchall()
               for res in qres:
                   queryResultList.append(res)                    
                   row_count = row_count + dbcursor.rowcount
                   #print(row_count)
                   
           print(colorama.Fore.YELLOW+'\n---------------- Database Query Result ----------------- '+colorama.Fore.RESET)
           i=0
           for result in queryResultList:
               i = i+1
               print('### ', i, '### ', result)
           print('----------------------------------------------------------\n ') 
           
           ans_reply = ''
           ans_id = 0 
           response_count = 0
           if (row_count ==0):
               # retrun empty for Web Search and DRNN functions 
               ans_reply = '' 
           elif (row_count ==1):
               ans_id = queryResultList[0][0]
               response_count = queryResultList[0][1]
               ans_reply = queryResultList[0][4]                            
           else:
               # Identify records that are duplicate
               #ans_reply = [item for item, count in collections.Counter(queryResultList).items() if count > 1]
               #ans_id = ans_reply[0][0]
               #response_count = queryResultList[0][1]
               #ans_reply = ans_reply[0][4]
               
               # Remove duplicate records 
               print(colorama.Fore.YELLOW+'\n---------------- After Removing Duplicate Records ----------------- '+colorama.Fore.RESET)
               no_duplicate = set(queryResultList)
               print(set(queryResultList)) 
                
               if(len(no_duplicate) > 1):
                   print(colorama.Fore.YELLOW+'\nFound more than one records'+colorama.Fore.RESET)
                   response = sqlforMinimizeRecords(nounEntityList, no_duplicate, dbcursor) 
                   ans_id = response[0][0]
                   response_count = response[0][1]
                   ans_reply = response[0][4]
            
               elif(len(no_duplicate) == 1):
                   # After removing duplicate, if only one record
                   ans_id = queryResultList[0][0]
                   response_count = queryResultList[0][1]
                   ans_reply = queryResultList[0][4]
               else:
                   ans_reply = ''                            
           
           # Update databse that how many times question being answered  
           
           # Calculate Jaccard similarity
           similarity_ratio = token_match(user_input_text, ans_reply)
           print(ans_reply,"\t", similarity_ratio)
    
        return ans_reply
    
    except Error as e:
        print ("Error while connecting to MySQL", e)
    finally:
        # Closing database connection
        if(connection.is_connected()):
            dbcursor.close()
            connection.close()
            #print("MySQL connection is closed")

def token_match(a, b):
    # Question-> tokens_a --> target_sentence  
    tokens_a = [token.lower().strip(string.punctuation) for token in nltk.tokenize.word_tokenize(a) \
                if token.lower().strip(string.punctuation) ]
    # Answers -> tokens_b -> ans_sentence 
    word_token_b = [token.lower().strip(string.punctuation) for token in nltk.tokenize.word_tokenize(b) \
                if token.lower().strip(string.punctuation) ]
                
    # Tokenization, Lemmatization and Removing Words 
    filtered_sentence = [w for w in word_token_b if not w in stop_words] 
    filtered_stop_words = [] 
    for w in word_token_b: 
        if w not in stop_words: 
            filtered_stop_words.append(w) 
    tokens_b = [] 
    for word in filtered_stop_words:
        tokens_b.append(wordnet_lemmatizer.lemmatize(word, pos="v")) 
    
    print('a--> ', tokens_a)
    print('b-->', tokens_b) 
    # Calculate Jaccard similarity
    ratio = len(set(tokens_a).intersection(tokens_b)) / float(len(set(tokens_a).union(tokens_b)))
    
    return ratio


def sqlforMinimizeRecords(nounEntityList, no_duplicate, dbcursor):
    ans_reply= []
    row_count = 0
    
    if(len(nounEntityList) ==1):
        nounEntityList.append(nounEntityList[0])
        
    # Loop all entities through SQL 
    for entity in nounEntityList:
        mysqlstatement = 'SELECT id, response_count, tag_id, question, response_message, keywords, message_type FROM knowledgebase WHERE question like\'%'+entity+'%\' OR keywords like\'%'+entity+'%\' OR response_message like\'%'+entity+'%\' HAVING response_message like\'%'+nounEntityList[0]+'%\' AND response_message like\'%'+nounEntityList[1]+'%\'  '
        dbcursor.execute(mysqlstatement)
        qres = dbcursor.fetchall()
        row_count = dbcursor.rowcount
        
    if (row_count >0):
        print(colorama.Fore.YELLOW+'---------------- SQL for Minimize Records ----------------- '+colorama.Fore.RESET)
        print(qres)
        ans_reply = qres
        print('------------------------------------------------------------\n ')
        
    return ans_reply
       
if __name__ == '__main__':
    print (kdd_search('Knowledge-based (KDD)Search'))
