import sqlite3

def create_database(): #создание базы данных для хранения пользовательских настроек
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS user
                    (url TEXT, 
                    token TEXT,
                    language TEXT)
                """)
    con.commit()

def insert_userdata(userdata): #вставка пользовательских настроек
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    cursor.execute("INSERT INTO user (url, token, language) VALUES (?, ?, ?)", userdata)
    con.commit()

def get_language(): #получаем токен пользователя
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    cursor.execute("SELECT language FROM user")
    user_language = cursor.fetchone()
    return user_language

def get_token(): #получаем язык, который выбрал пользователь
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    cursor.execute("SELECT token FROM user")
    token = cursor.fetchone()
    return token


