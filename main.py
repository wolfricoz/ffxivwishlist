import json

from data.Item import Item
from data.Servers import Servers
datacenters = ('Chaos', 'Light')  # Example datacenters, can be modified as needed
if __name__ == "__main__" :
	servers = Servers()
	with open("data/items.json", 'r') as f :
		items = json.load(f)
		with open('results.txt', 'w') as w :
			for key, value in items.items() :
				item = Item(key, value)
				print(f"Processing {key} with max price {value}")
				w.write(f"\n{key} (max price: {value - (value * 0.05)}): \n")
				for datacenter in datacenters :
					w.write("\n" + item.get_items_by_datacenter(datacenter))
				print(f"Finished {key}")
