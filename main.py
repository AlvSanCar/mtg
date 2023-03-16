import requests 
import json

# URL base de la API de Magic the Gathering
base_url = "https://api.magicthegathering.io/v1/cards"

# Parámetros de la solicitud
params = {"language":"es","pageSize": 100} # El número máximo de resultados por página es 100

# Lista para almacenar todas las cartas
all_cards = []

# Bucle para obtener todas las páginas de resultados
while True:
    response = requests.get(base_url, params=params)
    data = json.loads(response.text)
    cards = data["cards"]
    all_cards.extend(cards)
    if len(cards) < 100:
        break
    params["page"] = params.get("page", 0) + 1
    

# Almacenar todas las cartas en un archivo JSON
with open("all_cards.json", "w") as f:
    json.dump(all_cards, f)
print ("Fin")