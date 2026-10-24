import requests

url = "https://api.weatherapi.com/v1/current.json?key=41289589ed334ddc97695843262410&q=London"

response = requests.get(url)

print(response.status_code)
if response.status_code == 200:
    print(response.json())



import requests

location = input("Enter your city:")

url = "https://api.weatherapi.com/v1/current.json?key=41289589ed334ddc97695843262410&q={location}"

response = requests.get(url)


print(response.status_code)
if response.status_code == 200:
    data = response.json()
    print(data["current"]["temp_c"])
    print(data["current"]["condition"]["text"])
    print(f" in {location},The weather is {data["current"]["temp_c"]} degrees celcius , and the weather is {data["current"]["condition"]["text"]} temperature")
   