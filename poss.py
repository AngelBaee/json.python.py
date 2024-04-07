import json

lol = {
    "name": "Sam",
    "age": "35",
    "married": True,
    "divorced": False,
    "children":("lily","Dan"),
    "pets": None,
    "cars": [
        {"model": "BMW M5", "mpg":27.5},
        {"model": "Ford MUstang", "mpg": 28.1}
    ]

}

print(json.dumps(lol))