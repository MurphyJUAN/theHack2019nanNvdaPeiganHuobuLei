import mysql.connector

# Knowledge-based (KB)Search
def knowledge_search(message):    
    
    # Connect to MySQL Database 
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="soho123",
      database="aichatbot"
    )
    dbcursor = mydb.cursor()
    
    mysqlstatement = 'SELECT template FROM knowledgebase WHERE pattern like\'%'+message+'%\''
    dbcursor.execute(mysqlstatement)
    result = dbcursor.fetchone()
    row_count = dbcursor.rowcount
    #print row_count
    myresult = ''
    if row_count >0:
        myresult = result[0]
                
    return myresult


if __name__ == '__main__':
    print(knowledge_search('AIChatbot'))
