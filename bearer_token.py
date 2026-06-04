import requests

BASE_URL = "https://reqres.in/api"

HEADERS = {
    "x-api-key": "free_user_3DiD0PjayLI0UTgdJclTFhOPZ06",
    "Content-Type": "application/json"
}


def get_auth_token():

    creds = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    response = requests.post(
        f"{BASE_URL}/login",
        json=creds,
        headers=HEADERS
    )

    print("Status Code:", response.status_code)

    print("Response:", response.json())

    data = response.json()

    return data["token"]


token = get_auth_token()

print("Generated Token:", token)


headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get(
    f"{BASE_URL}/users/2",
    headers=HEADERS
)

print(response.status_code)

print(response.json())