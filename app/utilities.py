import os, requests
from pathlib import Path
from dotenv import load_dotenv
from fastapi import Request

BASE_DIR = Path(__file__).resolve().parent.parent

def get_env_value(key):
    '''Returns the value of an environment variable'''

    load_dotenv(os.path.join(BASE_DIR, '.env'))
    return os.getenv(key)


def get_client_ip(request: Request):
    '''Returns the IP address of current client'''

    x_forwarded_for = request.headers.get('X-Forwarded-For')
    if x_forwarded_for:
        client_ip = x_forwarded_for.split(',')[0]
    else:
        client_ip = request.client.host
        
    return client_ip


def get_ip_info():
    '''Returns the location of the client'''

    response = requests.get(f"https://ipinfo.io?token={get_env_value('IPINFO_APIKEY')}")

    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        return None
    

def get_weather_data(lat, long):
    '''Returns the weather data of the user;s current location'''

    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid={get_env_value('OPENWEATHER_MAP_APIKEY')}&units=metric")

    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        return None



