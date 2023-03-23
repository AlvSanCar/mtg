import requests 
import json
import pymongo

# URL base de la API de Magic the Gathering
def get_cards(): 
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

def db_connection():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    myDB = client.get_database("mtg")
    cards = myDB.get_collection("cardlist")
    if(len(cards) == 0):
        print("no hay cartas todavía")
    else:
        print("hay cartas")

db_connection()