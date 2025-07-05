import json
import threading
from time import sleep

from data.Item import Item
from data.Servers import Servers

datacenters = ('Chaos', 'Light')  # Example datacenters, can be modified as needed

# Potentially speed this up by making less requests by requesting all items at once
if __name__ == "__main__" :
	servers = Servers()
	with open("data/items.json", 'r') as f :
		items = json.load(f)
		# Sort the dictionary by name
		items = dict(sorted(items.items()))
		with open('results.txt', 'w') as w :
			for key, value in items.items() :
				item = Item(key, value)
				print(f"Processing {key} with max price {value}")
				w.write(f"\n{key} (max price: {value - (value * 0.05)}): \n")
				for datacenter in datacenters :
					w.write("\n" + item.get_items_by_datacenter(datacenter))
				print(f"Finished {key}")
