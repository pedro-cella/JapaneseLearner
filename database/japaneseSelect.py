import sqlite3

def get_hiragana():
    conn = sqlite3.connect('japanese.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM hiragana')
    results = cursor.fetchall()
    conn.close()
    return results

def get_katakana():
    conn = sqlite3.connect('japanese.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM katakana')
    results = cursor.fetchall()
    conn.close()
    return results

print(get_hiragana())
print(get_katakana())