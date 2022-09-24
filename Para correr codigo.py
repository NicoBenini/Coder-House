import requests


mi_data = requests.get("https://jsonplaceholder.typicode.com/users")

mi_lista = mi_data.json()

for user in mi_lista:
    print("*" * 90)
    
