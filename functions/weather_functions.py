import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Funciones relacionadas con el clima

def get_secret(key):
    """
    Obtiene un secreto almacenado de forma segura.
    """
    return os.getenv(key)

def get_weather_data(city):
    """
    Obtiene los datos del clima para una ciudad dada.
    """
    api_key = get_secret("API_KEY")
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Lanza una excepción si la solicitud no fue exitosa
        data = response.json()

        temp = round(data['main']['temp'] - 273.15, 1)  # Temperatura en Celsius con un decimal
        temp_feel = round(data['main']['feels_like'] - 273.15, 1)
        min_temp = round(data['main']['temp_min'] - 273.15, 1)
        max_temp = round(data['main']['temp_max'] - 273.15, 1)

        return {
            "city": city,
            "condition": data['weather'][0]['main'],
            "temp": temp,
            "temp_feel": temp_feel,
            "min_temp": min_temp,
            "max_temp": max_temp
        }
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener los datos del clima para {city}: {e}")
        return None

def weather_summary(city, units="metric"):
    """
    Crea un resumen del tiempo para una ciudad dada.
    La unidad predeterminada es Celsius.
    """
    data = get_weather_data(city)
    if data:
        city = data['city']
        condition = data['condition']
        temp = data['temp']
        temp_feel = data['temp_feel']
        min_temp = data['min_temp']
        max_temp = data['max_temp']

        summary = f"El tiempo en {city} es {condition} con una temperatura de {temp}°C. La sensación térmica es de {temp_feel}°C. La temperatura mínima es de {min_temp}°C y la máxima de {max_temp}°C."
        return summary
    else:
        return "No se pudo obtener el resumen del tiempo debido a un error."

# Ejemplo de uso
# print(get_weather_data("Madrid"))
# print(weather_summary("Madrid"))
