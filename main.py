import json

from data.Item import Item
from data.Servers import Servers

if __name__ == "__main__" :
	servers = Servers()
	with open("data/items.json", 'r') as f :
		items = json.load(f)
		print(items)
		with open('results.txt', 'w') as w :
			for key, value in items.items() :
				item = Item(key, value)
				w.write(str(item) + "\n\n")
				print(f"Finished {key}")
