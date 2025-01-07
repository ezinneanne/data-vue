import requests

url = "http://localhost:5000/predict"
data = {
    "pH": 7.91,
    "N": 46.29,
    "P": 5.07,
    "K": 100.96,
    "OC": 0.12,
    "Particles": 1.14,
    "Water_holding_content": 1.36,
    "Soil_type": "Sandy"
}

response = requests.post(url, json=data)
print(response.json())
