import sqlite3

def setup_database():
    connection = sqlite3.connect('weather.db')
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS weather_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city TEXT,
        main TEXT,
        temp REAL,
        feels_like REAL,
        dt INTEGER
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS daily_summary (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city TEXT,
        avg_temp REAL,
        max_temp REAL,
        min_temp REAL,
        dominant_condition TEXT,
        date TEXT
    )''')

    connection.commit()
    connection.close()

if __name__ == '__main__':
    setup_database()

