import requests

def main():
    api_key = "PUT_YOUR_API_KEY_HERE"

    city = input("Give city name: ")

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key
    }

    response = requests.get(url, params=params)
    data = response.json()
    description = data["weather"][0]["description"]
    temp_kelvin = data["main"]["temp"]
    temp_celsius = temp_kelvin - 273.15

    print(f"Weather in {city}: {description}")
    print(f"Temperature: {temp_celsius:.1f} °C")

if __name__ == "__main__":
    main()