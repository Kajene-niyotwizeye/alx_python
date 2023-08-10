import sys
import requests

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py <URL> <email>")
        return

    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}
    response = requests.post(url, data=payload)

    print("Response body:")
    print(response.text)

if __name__ == "__main__":
    main()

