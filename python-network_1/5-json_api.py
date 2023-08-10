import sys
import requests

def search_user(letter):
    url = "http://0.0.0.0:5000/search_user"
    params = {"q": letter}

    response = requests.post(url, data=params)

    try:
        json_data = response.json()
        if json_data:
            user_id = json_data.get("id")
            user_name = json_data.get("name")
            print(f"[{user_id}] {user_name}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""
    search_user(letter)

