import requests

endpoint = "http://localhost:8000/api/"

get_reponse = requests.post(endpoint, json={"title": "Some title", "content": "Hello world"})

print(get_reponse.json())