import logging

import requests

from methods.singleton import Singleton


class Servers (metaclass=Singleton):
	servers: list = []

	def __init__(self, targets = ('Chaos', 'Light')):
		print("fetching servers")
		datacenters = requests.get("https://xivapi.com/servers/dc").json()
		for target in targets:
			servers = datacenters[target]
			for server in servers:
				self.servers.append(server)


