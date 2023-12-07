import requests
def fetch_random_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)

    if response.status_code == 200:
        joke_data = response.json()
        return joke_data.get("value")
    else:
        return "Failed to fetch Chuck Norris joke"
def main():
    print("Fetching a random Chuck Norris joke...\n")
    joke = fetch_random_joke()
    print(joke)
if __name__ == "__main__":
    main()
