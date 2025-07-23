import requests

url = "http://127.0.0.1:5000/add_product"
data = {
    "name": "Mouse",
    "quantity": 5,
    "price": 99.99,
    "category": "Electronics"
}

response = requests.post(url, json=data)
print(response.status_code)
print(response.json())
