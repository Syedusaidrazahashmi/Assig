import requests

BASE_URL = "http://127.0.0.1:8000"

def get_all_assignments():
    res = requests.get(f"{BASE_URL}/assignments")
    return res.json()["assignments"]

def add_assignment(title, subject, description, due_date):
    data = {"title": title, "subject": subject, "description": description, "due_date": due_date}
    return requests.post(f"{BASE_URL}/assignments", params=data).json()

def get_assignment(aid: int):
    return requests.get(f"{BASE_URL}/assignments/{aid}").json()

def update_assignment(aid, title=None, subject=None, description=None, due_date=None, submitted=None, grade=None):
    data = {"title": title, "subject": subject, "description": description, "due_date": due_date,
            "submitted": submitted, "grade": grade}
    return requests.put(f"{BASE_URL}/assignments/{aid}", params=data).json()

def delete_assignment(aid: int):
    return requests.delete(f"{BASE_URL}/assignments/{aid}").json()
