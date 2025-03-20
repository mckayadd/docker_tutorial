import requests

API_URL = "http://prime-checker:8000/check_prime/"

def check_prime(number):

    response = requests.post(API_URL, json = {"number": number})
    if response.status_code == 200:
        data = response.json()
        print("✅ {data['number']} is {'a prime' if data['is_prime'] else 'not a prime'} number.")
    else:
        print("❌ Error connecting to API.")

if __name__ == "__main__":
    number = int(input("Enter a number to check: "))
    check_prime(number)