# database.py

import sqlite3

def init_db():
    conn = sqlite3.connect("bot.db")
    cursor = conn.cursor()

    # Таблицы: разделы, темы, файлы
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sections (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name_ru TEXT,
        name_uz TEXT
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS topics (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        section_id INTEGER,
        name_ru TEXT,
        name_uz TEXT,
        FOREIGN KEY (section_id) REFERENCES sections(id)
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS files (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        topic_id INTEGER,
        file_id TEXT,
        file_name TEXT,
        file_type TEXT,
        FOREIGN KEY (topic_id) REFERENCES topics(id)
    )""")

    conn.commit()
    conn.close()
