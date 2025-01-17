# -*- coding: utf-8 -*-

import requests
import sqlite3
import schedule
import time
from config import API_KEY, CITIES

def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return {
        "city": city,
        "main": data['weather'][0]['main'],
        "temp": data['main']['temp'] - 273.15,  # Convert from Kelvin to Celsius
        "feels_like": data['main']['feels_like'] - 273.15,  # Convert from Kelvin to Celsius
        "dt": data['dt']
    }

def store_weather_data(data):
    connection = sqlite3.connect('weather.db')
    cursor = connection.cursor()

    cursor.execute('''
    INSERT INTO weather_data (city, main, temp, feels_like, dt)
    VALUES (?, ?, ?, ?, ?)''', (data['city'], data['main'], data['temp'], data['feels_like'], data['dt']))

    connection.commit()
    connection.close()

def aggregate_daily_data():
    # Implement daily data aggregation logic here
    pass

def fetch_and_store_weather():
    for city in CITIES:
        data = fetch_weather(city)
        store_weather_data(data)
        print(f"Stored weather data for {city}")

schedule.every(5).minutes.do(fetch_and_store_weather)
schedule.every().day.at("00:00").do(aggregate_daily_data)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
