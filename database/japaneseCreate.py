import sqlite3

def create_database():
    conn = sqlite3.connect('japanese.db')
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS hiragana(
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      romaji TEXT NOT NULL,
                      kana TEXT NOT NULL)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS katakana(
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      romaji TEXT NOT NULL,
                      kana TEXT NOT NULL)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS words(
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      word TEXT NOT NULL,
                      kana_type TEXT NOT NULL)''')
    
    conn.commit()
    conn.close()
    
create_database()