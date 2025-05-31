import logging

import requests

from methods.singleton import Singleton


class Servers (metaclass=Singleton):
	servers: dict = {}

	def __init__(self, targets = ('Chaos', 'Light')):
		print("fetching servers")
		datacenters = requests.get("https://universalis.app/api/v2/data-centers").json()
		worlds = requests.get("https://universalis.app/api/v2/worlds").json()

		for datacenter in datacenters:
			name = datacenter.get('name')
			if datacenter.get('name') not in targets:
				continue
			self.servers[name] = []
			for world in worlds:
				if world.get('id') in datacenter.get('worlds'):
					self.servers[name].append(world.get('name'))
			self.servers[name].sort()
		if not datacenters or not worlds:
			logging.error("Failed to fetch servers")
			return



