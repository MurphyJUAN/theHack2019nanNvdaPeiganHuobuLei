import mysql.connector

# Save Chat History in Database 
def chat_history(message):    
    
    # Connect to MySQL Database 
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="soho123",
      database="aichatbot"
    )
    dbcursor = mydb.cursor()
    
    sql = 'INSERT INTO customers (name, address) VALUES (%s, %s)'
    val = ("John", "Highway 21")
    dbcursor.execute(sql, val)
    mydb.commit()
    
    return 'Record inserted.'


if __name__ == '__main__':
    print (chat_history('Chat History'))
