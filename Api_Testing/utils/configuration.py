import configparser
import sqlite3
def getConfig():
    config = configparser.ConfigParser()
    config.read('utils\properties.ini')
    return config
print(type(getConfig()['SQL']['database']))
def getConnection():
    try:
        conn = sqlite3.connect(getConfig()['SQL']['database'])
        print('connected successfully.......')
        return conn
    except sqlite3.Error as e:
        print('database not connected!!!!', e)

def getQuery(query):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()
    return row

    
