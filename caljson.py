import json

with open('chaldal-category.json') as f:
	data = f.read()

js = json.loads(data)

print js['CategoryService']['categories'][0]