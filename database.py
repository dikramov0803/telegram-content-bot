import sqlite3

def init_db():
    conn = sqlite3.connect("bot.db")
    c = conn.cursor()

    # Пользователи
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            language TEXT
        )
    ''')

    # Разделы
    c.execute('''
        CREATE TABLE IF NOT EXISTS sections (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name_ru TEXT,
            name_uz TEXT
        )
    ''')

    # Темы
    c.execute('''
        CREATE TABLE IF NOT EXISTS topics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            section_id INTEGER,
            name_ru TEXT,
            name_uz TEXT,
            FOREIGN KEY (section_id) REFERENCES sections(id)
        )
    ''')

    # Файлы
    c.execute('''
        CREATE TABLE IF NOT EXISTS files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic_id INTEGER,
            file_type TEXT,
            file_id TEXT,
            caption TEXT,
            FOREIGN KEY (topic_id) REFERENCES topics(id)
        )
    ''')

    conn.commit()
    conn.close()
