import sqlite3
from kanas import HIRAGANA, KATAKANA

def insert_database():
    conn = sqlite3.connect('japanese.db')
    cursor = conn.cursor()
    
    # Insert hiragana
    cursor.executemany('INSERT INTO hiragana(romaji, kana) VALUES (?, ?)', HIRAGANA)
    
    # Insert katakan
    cursor.executemany('INSERT INTO katakana(romaji, kana) VALUES (?, ?)', KATAKANA)
    
    conn.commit()
    conn.close()
    
insert_database()