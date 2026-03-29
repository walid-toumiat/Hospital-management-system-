import sqlite3

# اسم ملف قاعدة البيانات الذي سيتم إنشاؤه
DB_NAME = "hospital_database.db"

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    # إنشاء الجدول باسم patients
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            illness TEXT NOT NULL,
            room INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# تهيئة القاعدة فور استدعاء الملف
init_db()
