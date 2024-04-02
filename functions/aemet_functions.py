import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
import json

load_dotenv()

estado_cielo_dict = {
    "11": "Despejado",
    "12": "Poco nuboso",
    "13": "Intervalos nubosos",
    "14": "Nuboso",
    "15": "Muy nuboso",
    "16": "Cubierto",
    "17": "Nubes altas",
    "18": "Nubes medias",
    "19": "Niebla",
    "20": "Niebla con bancos de niebla",
    "21": "Niebla con bancos de niebla",
    "22": "Niebla con bancos de niebla",
    "23": "Niebla con bancos de niebla",
    "24": "Niebla con bancos de niebla",
    "25": "Muy nuboso con lluvia",
    "26": "Nuboso con lluvia",
    "27": "Cubierto con lluvia",
    "28": "Despejado con lluvia",
    "29": "Poco nuboso con lluvia",
    "30": "Intervalos nubosos con lluvia",
    "31": "Intervalos nubosos con lluvia",
    "32": "Intervalos nubosos con lluvia",
    "33": "Intervalos nubosos con lluvia",
    "34": "Intervalos nubosos con lluvia",
    "35": "Intervalos nubosos con lluvia",
    "36": "Intervalos nubosos con lluvia",
    "37": "Intervalos nubosos con lluvia",
    "38": "Intervalos nubosos con lluvia",
    "39": "Intervalos nubosos con lluvia",
    "40": "Intervalos nubosos con lluvia",
    "41": "Intervalos nubosos con lluvia",
    "42": "Intervalos nubosos con lluvia",
    "43": "Intervalos nubosos con lluvia",
    "44": "Nuboso con lluvia escasa",
    "45": "Muy nuboso con lluvia escasa",
    "46": "Intervalos nubosos con lluvia escasa",
    "47": "Intervalos nubosos con lluvia escasa",
    "48": "Intervalos nubosos con lluvia escasa",
    "49": "Intervalos nubosos con lluvia escasa",
    "50": "Intervalos nubosos con lluvia escasa",
    "51": "Intervalos nubosos con lluvia escasa",
    "52": "Intervalos nubosos con lluvia escasa",
    "53": "Intervalos nubosos con lluvia escasa",
    "54": "Intervalos nubosos con lluvia escasa",
    "55": "Muy nuboso con lluvia",
    "56": "Cubierto con lluvia",
    "57": "Nuboso con lluvia",
    "58": "Despejado con lluvia",
    "59": "Poco nuboso con lluvia",
    "60": "Intervalos nubosos con lluvia",
    "61": "Intervalos nubosos con lluvia",
    "62": "Intervalos nubosos con lluvia",
    "63": "Intervalos nubosos con lluvia",
    "64": "Intervalos nubosos con lluvia",
    "65": "Intervalos nubosos con lluvia",
    "66": "Intervalos nubosos con lluvia",
    "67": "Intervalos nubosos con lluvia",
    "68": "Intervalos nubosos con lluvia",
    "69": "Intervalos nubosos con lluvia",
    "70": "Intervalos nubosos con lluvia",
    "71": "Intervalos nubosos con lluvia",
    "72": "Intervalos nubosos con lluvia",
    "73": "Intervalos nubosos con lluvia",
    "74": "Intervalos nubosos con lluvia",
    "75": "Intervalos nubosos con lluvia",
    "76": "Intervalos nubosos con lluvia",
    "77": "Intervalos nubosos con lluvia",
    "78": "Intervalos nubosos con lluvia",
    "79": "Intervalos nubosos con lluvia",
    "80": "Intervalos nubosos con lluvia",
    "81": "Intervalos nubosos con lluvia",
    "82": "Intervalos nubosos con lluvia",
    "83": "Intervalos nubosos con lluvia",
    "84": "Intervalos nubosos con lluvia",
    "85": "Intervalos nubosos con lluvia",
    "86": "Intervalos nubosos con lluvia",
    "87": "Intervalos nubosos con lluvia",
    "88": "Intervalos nubosos con lluvia",
    "89": "Intervalos nubosos con lluvia",
    "90": "Intervalos nubosos con lluvia",
    "91": "Intervalos nubosos con lluvia",
    "92": "Intervalos nubosos con lluvia",
    "93": "Intervalos nubosos con lluvia",
    "94": "Intervalos nubosos con lluvia",
    "95": "Intervalos nubosos con lluvia",
    "96": "Intervalos nubosos con lluvia",
    "97": "Intervalos nubosos con lluvia",
    "98": "Intervalos nubosos con lluvia",
    "99": "Intervalos nubosos con lluvia"
}


def get_secret(key):
    """
    Obtiene un secreto almacenado de forma segura.
    """
    return os.getenv(key)

def get_weather_data():
    """
    Obtiene los datos de predicion del clima para Mondejar.
    """
    url = "https://opendata.aemet.es/opendata/api/prediccion/especifica/municipio/diaria/19192"

    api_key = get_secret("aemetkey")

    querystring = {"api_key": api_key}

    response = requests.get(url, params=querystring)

    if response.status_code == 200:
        data = response.json()
        datos_url = data["datos"]
        response_datos = requests.get(datos_url)
        if response_datos.status_code == 200:
            with open("prediccion_diaria.json", "w", encoding="utf-8") as file:
                file.write(response_datos.text)
                print("Datos de la predicción diaria guardados exitosamente")
                return "Datos de la predicción diaria guardados exitosamente"
        else:
            print("Error al obtener los datos de la predicción")
            return "Error al obtener los datos de la predicción"
    else:
        print("Error al obtener la URL de los datos de la predicción")
        return "Error al obtener la URL de los datos de la predicción"
  

def predict_weather():
    # Primero, mira si los datos de la predicción diaria están disponibles
    if not os.path.exists("prediccion_diaria.json"):
        get_weather_data()
    
    # Lee los datos de la predicción diaria
    with open("prediccion_diaria.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    # Busca la predicción para el día actual
    today = datetime.now().date().isoformat()
    for prediction in data:
        if prediction["prediccion"]["dia"] == today:
            fecha_str = datetime.strptime(today, "%Y-%m-%d").strftime("%A %d de %B de %Y")
            estado_cielo = estado_cielo_dict[prediction["prediccion"]["estadoCielo"]]
            temp_max = prediction["prediccion"]["temperatura"]["maxima"]
            temp_min = prediction["prediccion"]["temperatura"]["minima"]

            mensaje = f"El tiempo para Mondejar el {fecha_str} será {estado_cielo} con temperaturas entre {temp_min}°C y {temp_max}°C."
            
            return mensaje

    # Si no se encuentra la predicción para el día actual
    return "No se encontraron datos de predicción para el día actual"
