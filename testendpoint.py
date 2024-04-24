import requests

# Base URL de la API
base_url = "http://localhost:8080" 

# Función para testear el endpoint / base
def test_base():
    url = base_url
    response = requests.get(url)
    print(f"Status Code for /: {response.status_code}")
    print(f"Response Text for /: {response.text}\n")

# Función para testear el endpoint /crypto/{crypto}
def test_crypto(crypto):
    url = f"{base_url}/crypto/{crypto}"
    response = requests.get(url)
    print(f"Status Code for /crypto/{{crypto}}: {response.status_code}")
    print(f"Response Text for /crypto/{{crypto}}: {response.text}\n")

# Función para testear el endpoint /crypto/{crypto}/price
def test_crypto_price(crypto):
    url = f"{base_url}/crypto/{crypto}/price"
    response = requests.get(url)
    print(f"Status Code for /crypto/{{crypto}}/price: {response.status_code}")
    print(f"Response Text for /crypto/{{crypto}}/price: {response.text}\n")

# Función para testear el endpoint /metro
def test_metro():
    url = f"{base_url}/metro"
    response = requests.get(url)
    print(f"Status Code for /metro: {response.status_code}")
    print(f"Response Text for /metro: {response.text}\n")

# Función para testear el endpoint /miestacion
def test_miestacion():
    url = f"{base_url}/miestacion"
    response = requests.get(url)
    print(f"Status Code for /miestacion: {response.status_code}")
    print(f"Response Text for /miestacion: {response.text}\n")

# Función para testear el endpoint /news
def test_news():
    url = f"{base_url}/news"
    response = requests.get(url)
    print(f"Status Code for /news: {response.status_code}")
    print(f"Response Text for /news: {response.text}\n")

# Función para testear el endpoint /stocks
def test_all_stocks():
    url = f"{base_url}/stocks"
    response = requests.get(url)
    print(f"Status Code for /stocks: {response.status_code}")
    print(f"Response Text for /stocks: {response.text}\n")

# Función para testear el endpoint /weather/{city}
def test_weather(city):
    url = f"{base_url}/weather/{city}"
    response = requests.get(url)
    print(f"Status Code for /weather/{{city}}: {response.status_code}")
    print(f"Response Text for /weather/{{city}}: {response.text}\n")

# Función para testear el endpoint /hora
def test_time():
    url = f"{base_url}/hora"
    response = requests.get(url)
    print(f"Status Code for /hora: {response.status_code}")
    print(f"Response Text for /hora: {response.text}\n")

# Función para testear el endpoint /fecha
def test_date():
    url = f"{base_url}/fecha"
    response = requests.get(url)
    print(f"Status Code for /fecha: {response.status_code}")
    print(f"Response Text for /fecha: {response.text}\n")

# Función para testear el endpoint /dia
def test_datetime():
    url = f"{base_url}/dia"
    response = requests.get(url)
    print(f"Status Code for /dia: {response.status_code}")
    print(f"Response Text for /dia: {response.text}\n")

# Ejecutar pruebas
# test_base()
# test_crypto("bitcoin")
# test_crypto_price("bitcoin")
# test_metro()
# test_miestacion()
# test_news()
# test_all_stocks()
# test_weather("Madrid")
# test_time()
# test_date()
# test_datetime()