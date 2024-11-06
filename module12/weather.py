import requests

api_key = "XXXX"

while True:
    kaupunki = input("Anna kaupungin nimi: ")

    url = f"http://api.openweathermap.org/data/2.5/weather?q={kaupunki}&appid={api_key}"

    vastaus = requests.get(url)

    if vastaus.status_code == 200:
        data = vastaus.json()
        lampotila_kelvin = data["main"]["temp"]
        lampotila_celsius = lampotila_kelvin - 273.15
        saatila = data["weather"][0]["description"]

        print(f"lämpötila: {lampotila_celsius:.1f} Celcius")
        print(f"kuvaus: {saatila}")