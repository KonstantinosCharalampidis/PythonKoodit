import requests, json
keyword = input("Enter keyword for the shows you are going to search: ")
request = "https://api.tvmaze.com/search/shows?q=" + keyword
try:
    response = requests.get(request)
    if response.status_code == 200:
        json_string = response.json()
        for a in json_string:
            print(a["show"]["name"])

except requests.exceptions.RequestException as e:
    print("Request could not be completed.")

