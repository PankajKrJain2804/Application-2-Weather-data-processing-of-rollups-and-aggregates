# -*- coding: utf-8 -*-

from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    connection = sqlite3.connect('weather.db')
    connection.row_factory = sqlite3.Row
    return connection

@app.route("/weather")
def weather():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM weather_data ORDER BY dt DESC LIMIT 1")
    row = cursor.fetchone()
    connection.close()
    return jsonify(dict(row))

@app.route("/summary")
def summary():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM daily_summary ORDER BY date DESC LIMIT 1")
    row = cursor.fetchone()
    connection.close()
    return jsonify(dict(row))

if __name__ == "__main__":
    app.run(debug=True)
