import requests

BASE = "http://127.0.0.1:8000"

# GET all books
print("GET /books ->", requests.get(f"{BASE}/books").json())

# POST new book
created = requests.post(f"{BASE}/books", json={"title": "The Lord of the Rings: The Fellowship of the Ring", "author": "J.R.R. Tolkien"})
print("POST /books ->", created.status_code, created.json())
new_id = created.json()["id"]

# GET single book
print(f"GET /books/{new_id} ->", requests.get(f"{BASE}/books/{new_id}").json())

# PUT update book
updated = requests.put(f"{BASE}/books/{new_id}", json={"title": "The Lord of the Rings: The Two Towers", "author": "J.R.R. Tolkien"})
print(f"PUT /books/{new_id} ->", updated.json())

# DELETE
deleted = requests.delete(f"{BASE}/books/{new_id}")
print(f"DELETE /books/{new_id} -> status", deleted.status_code)