import requests

# URL de la API
api_url = "http://localhost:8080/convertir_video/"

# URL del video de YouTube que deseas convertir a MP3
youtube_url = "https://www.youtube.com/watch?v=1P5BSm_oFJg&ab"

# Crear el cuerpo de la solicitud con la URL de YouTube
data = {"url": youtube_url}

print("Convirtiendo el video a MP3...", data)

# Enviar la solicitud POST a la API
response = requests.post(api_url, json=data)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Extraer la respuesta JSON de la API
    response_json = response.json()
    # Obtener la ruta del archivo MP3 convertido
    mp3_file_path = response_json["mp3_file_path"]
    print("El video se ha convertido a MP3 con éxito. Puedes descargarlo en:", mp3_file_path)
else:
    print("Ha ocurrido un error al procesar la solicitud:", response.text)
