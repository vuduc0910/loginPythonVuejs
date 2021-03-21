import mysql.connector
conn = mysql.connector.connect(host = "localhost", user = "root", 
    passwd = "123456789", database = "accountsdb")
def get_user(username,password):
    cur  = conn.cursor()
    try :
        cur.execute("SELECT permission FROM accounts WHERE username = '"+ username + "' and password = '"+ password + "'")
        result = cur.fetchall()
        return result
    except :
        conn.rollback()
    conn.close()
