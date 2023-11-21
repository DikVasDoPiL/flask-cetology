import requests

response = requests.post(
    "http://127.0.0.1:5000/adverts",
    json={
        "title": "HomeWork",
        "description": "Very hard homework",
        "owner": "Usver",
    },
)
print(response.status_code, response.json(), sep='\n', end='\n\n')

response = requests.post(
    "http://127.0.0.1:5000/adverts",
    json={
        "title": "Cup of tea",
        "description": "The hottect bugged tea",
        "owner": "Admin",
    },
)
print(response.status_code, response.json(), sep='\n', end='\n\n')

response = requests.post(
    "http://127.0.0.1:5000/adverts",
    json={
        "title": "Sale mansion",
        "description": "Super premium mansion in like-city village, for sale 11.11",
        "owner": "Monika",
    },
)
print(response.status_code, response.json(), sep='\n', end='\n\n')


response = requests.get("http://127.0.0.1:5000/adverts/1")
print(response.status_code, response.json(), sep='\n', end='\n\n')

response = requests.get("http://127.0.0.1:5000/adverts/2")
print(response.status_code, response.json(), sep='\n', end='\n\n')

response = requests.get("http://127.0.0.1:5000/adverts/3")
print(response.status_code, response.json(), sep='\n', end='\n\n')


response = requests.patch(
    "http://127.0.0.1:5000/adverts/3",
    json={
        "title": "Sale mansion, not for laffki!!",
        "description": "Super premium mansion in like-city village, for sale 11.11",
        "owner": "Monika",
    },
)

response = requests.get("http://127.0.0.1:5000/adverts/3")
print(response.status_code, response.json(), sep='\n', end='\n\n')

response = requests.delete("http://127.0.0.1:5000/adverts/2")
print(response.status_code, response.json(), sep='\n', end='\n\n')

response = requests.get("http://127.0.0.1:5000/adverts/3")
print(response.status_code, response.json(), sep='\n', end='\n\n')

