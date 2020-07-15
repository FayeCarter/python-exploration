from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def hello_world():

  if request.method == "POST":
    city = request.form['city']
    city = request.form['country']
    api_key = "e7b8d42f2fca6e9f0e129a23c6368d0e"
    weather_url = requests.get(f'###')

    weather_data = weather_url.json()

    temp = round(weather_data['main']['temp'])
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    
    return render_template("results.html", temp=temp, humidity=humidity, wind_speed=wid_speed, city="city")
  
  return render_template("index.html")