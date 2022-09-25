# example file to make requests to the API endpoints that require DB
# used to test and ensure that the DB works properly

import requests

# example values filled in
foo = {"name": "someone", "age": 69}

bar = {
    "title": "some fancy title",
    "rating": 10,
    "author": "amazing writer idk",
    "author_id": 2,
}

# assuming that you host in "127.0.0.1"
requests.post("http://127.0.0.1:5001/book/", json=bar)
requests.post("http://127.0.0.1:5001/author/", json=foo)
a = requests.get("http://127.0.0.1:5001/book/")
b = requests.get("http://127.0.0.1:5001/author/")
# just to access the data
print(b.json())
print(a.json())
