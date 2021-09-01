import requests
import json
import time
import sys


def get_ip():
    response = requests.get('https://ifconfig.co/json')
    ip_adress = response.json()['ip']
    return ip_adress


def get_data(location):
    key = 'e21041aaad1d4f0e9f9125822211507'
    responce = requests.get(f'http://api.weatherapi.com/v1/current.json?'
                            f'key= e21041aaad1d4f0e9f9125822211507&'
                            f'q={location}&aqi=no&lang=ru')
    data = responce.json()
    return data


def get_weather(data):
    city = data['location']['name']
    country = data['location']['country']
    time = data['location']['localtime']
    condition = data['current']['condition']['text']
    temperature = f"Температура: {data['current']['temp_c']}"
    feels_like = f"Ощущается как: {data['current']['feelslike_c']}\n"
    return (city, country, time, condition, temperature, feels_like)


weather = get_weather(get_data(get_ip()))
[print(i) for i in weather]
time.sleep(1.5)


