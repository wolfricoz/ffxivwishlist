from apis.universalis import Universalis
from apis.xivapi import xivapi
from data.Servers import Servers


class Item():
	item_name: str
	item_id: int
	available_items: dict = {

	}

	def __init__(self, name, max_price):
		self.item_name = name
		self.item_id = xivapi().get_item_id(name)
		self.max_price = max_price
		servers = Servers().servers
		for server in servers:
			count = 0
			listings = Universalis().get_listings(self.item_id, server)
			if not listings:
				continue
			for listing in listings :
				price = listing.get('pricePerUnit', 99999)
				# Incase tax needs to be enabled, leaving this here.
				tax = price * 0.05
				if price <= max_price :
					count += listing.get('quantity', 0)
			self.available_items[server] = count


	def __str__(self):
		return self.item_name + "\n" +"\n".join([f"{server} {self.max_price} : {count}" for server, count in self.available_items.items() if count > 0])