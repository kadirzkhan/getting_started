import os, time, requests
from dotenv import load_dotenv

'''load_dotenv(".env.local")
API = os.environ['BASE_URL']

s = requests.Session()
s.headers.update({
    "Authorization": f"Bearer {os.environ['GOREST_TOKEN']}",
    "Accept": "application/json",
    "Content-Type": "application/json",
})

r = s.get(f"{API}/users", params={"status": "active", "page": 1}, timeout=10)
r.raise_for_status()
users = r.json()
print(len(users), "users on this page")'''

'''def get_user(user_id):
    r = s.get(f"{API}/users/{user_id}", timeout=10)
    if r.status_code == 404:
        return None
    r.raise_for_status()
    return r.json()


def page_users(**filters):
    page = 1
    while True:
        r = s.get(f"{API}/users",
                  params={**filters, "page": page},
                  timeout=10)
        r.raise_for_status()
        batch = r.json()
        if not batch:
            return
        for user in batch:
            yield user
        total = int(r.headers.get("X-Pagination-Pages", 1))
        if page >= total:
            return
        page += 1

i = 0
for u in page_users(status="active"):
    i += 1
    print(u["email"])
print(f"Total users: {i}")'''