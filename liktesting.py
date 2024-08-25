import requests

url = 'http://127.0.0.1:5000/bfhl'
data = {
    "data": ["M", "1", "334", "4", "B", "Z", "a"]
}

response = requests.post(url, json=data)
print(response.json())
