import sqlite3

DB_NAME = "absensi.db"

def get_connection():
    return sqlite3.connect(DB_NAME)


def init_database():

    conn = get_connection()
    cursor = conn.cursor()

    # tabel users
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT NOT NULL,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )
    """)

    # tabel absensi
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS absensi(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        tanggal TEXT,
        jam_masuk TEXT,
        jam_pulang TEXT,
        status TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    conn.commit()
    conn.close()


def insert_default_data():

    conn = get_connection()
    cursor = conn.cursor()

    users = [
        ("Andi Pratama", "mahasiswa", "123", "mahasiswa"),
        ("Dr. Ahmad", "dosen", "123", "dosen")
    ]

    for user in users:
        try:
            cursor.execute("""
            INSERT INTO users(nama, username, password, role)
            VALUES (?, ?, ?, ?)
            """, user)
        except:
            pass

    conn.commit()
    conn.close()