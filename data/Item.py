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
		for dataserver in servers:
			self.available_items[dataserver] = {}
			for server in servers[dataserver]:
				count = 0
				listings = Universalis().get_listings(self.item_id, server)
				if not listings:
					continue
				for listing in listings :
					price = listing.get('pricePerUnit', 99999)
					# Incase tax needs to be enabled, leaving this here.
					tax = price * 0.05
					if price + tax<= max_price :
						count += listing.get('quantity', 0)
				self.available_items[dataserver][server] = count


	def __str__(self):
		return self.item_name + "\n" +"\n".join([f"{server} {self.max_price - (self.max_price * 0.05)} : {count}" for server, count in self.available_items.items() if count > 0])

	def get_items_by_datacenter(self, datacenter):
		items = f"{datacenter.upper()}\n"
		total = 0
		for server, count in self.available_items.get(datacenter, {}).items():
			if count > 0:
				items += f"{server}: {count}\n"
				total += count
		items += f"Total: {total}\n"
		return items
