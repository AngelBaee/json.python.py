#JSON is a text written with JavaScript object notation
import json

x = '{"name": "Jack", "age": 30, "city": "New York"}'
y = json.loads(x)

print(y["name"])