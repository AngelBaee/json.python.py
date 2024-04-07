import json

lol = {
    "name": "Bob",
    "age": 20,
    "city": "Washington"

}

olo = json.dumps(lol)

print(olo)