import requests

def main():
    url = "https://api.chucknorris.io/jokes/random"

    response = requests.get(url)
    data = response.json()

    joke = data["value"]
    print(joke)

if __name__ == "__main__":
    main()