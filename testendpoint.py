import requests

# URL de la API
api_url = "http://localhost:8080/hora"

# Hacer una petición GET a la API
response = requests.get(api_url)

# Imprimir el código de estado de la respuesta
print("Status Code: ", response.status_code)

# Imprimir el contenido de la respuesta
print("Response Text: ", response.text)