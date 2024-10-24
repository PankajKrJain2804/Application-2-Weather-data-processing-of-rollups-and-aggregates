# Application 2 : Real-Time Data Processing System for Weather Monitoring with Rollups and Aggregates

> Zeotap | Software Engineer Intern | Assignment | Application 2

# introduction

Hi, I'm Pankajkrjain , a Software Developer and AI enthusiast skilled in python, Kotlin/java, React, Next.js, Django, and machine learning. I'm currently working on projects as mobile music application and travellers Application integrated with safty features for navigation , always eager to learn!
[LinkedIn](https://www.linkedin.com/in/pankajkumar2849/). 

## Overview
This project is a real-time data processing system designed to monitor weather conditions using the OpenWeatherMap API. It collects weather data for major metros in India, processes the data to provide daily summaries, and triggers alerts based on user-defined thresholds.

## Features
- **Real-Time Data Collection**: Fetches weather data every 5 minutes.
- **Daily Weather Summaries**: Calculates and stores daily aggregates such as average, maximum, minimum temperatures, and dominant weather condition.
- **Alerting Mechanism**: Triggers alerts if certain weather thresholds are breached.
- **REST API Endpoints**: Provides endpoints to retrieve the latest weather data and daily summaries.

## Prerequisites
- Python 3.x
- Virtual environment

## Installation

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/PankajKrJain2804/weather-data-processing-of-rollups-and-aggregates.git

   
# Create and Activate a Virtual Environment:

sh

python -m venv venv
venv\Scripts\activate  # On Windows

- source venv/bin/activate  # On macOS/Linux

# Install Dependencies:

sh

pip install -r requirements.txt
Set Up the Database:

sh

python database.py
Add Your OpenWeatherMap API Key in config.py:

python

API_KEY = "your_openweathermap_api_key"
CITIES = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]
Usage
Run the Data Processing Script:

sh

python data_processing.py
Run the Flask App:

sh

python app.py
API Endpoints
Get Latest Weather Data
Endpoint: /weather

Method: GET

- Description: Retrieves the latest weather data from the database.

Get Daily Summary
Endpoint: /summary

Method: GET

- Description: Retrieves the latest daily weather summary from the database.

# Design Choices
SQLite Database: Chosen for simplicity and ease of use.

Flask Framework: Provides a lightweight web server and RESTful API.

Schedule Library: Used for scheduling periodic data fetching and aggregation tasks.

Testing
System Setup:

Verify that the system starts successfully and connects to the OpenWeatherMap API using a valid API key.

Data Retrieval:

Simulate API calls at configurable intervals and ensure the system retrieves weather data for the specified locations and parses the response correctly.

Temperature Conversion:

- Test the conversion of temperature values from Kelvin to Celsius (or Fahrenheit) based on user preference.

Daily Weather Summary:

- Simulate a sequence of weather updates for several days and verify that daily summaries are calculated correctly.

Alerting Thresholds:

- Define and configure user thresholds for temperature or weather conditions. Simulate weather data exceeding or breaching the thresholds and verify that alerts are triggered correctly.

- Future Enhancements
   Additional Weather Parameters: Extend the system to support humidity, wind speed, etc.

Weather Forecasts: Implement features to retrieve and summarize weather forecasts.
