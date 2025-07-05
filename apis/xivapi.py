import json
import os.path
from datetime import datetime

import requests


class xivapi():
	url = "https://v2.xivapi.com/api/"
	# TODO: Add a cache for this function, it's not very efficient to call this every time - the data doesn't change that often.

	def search(self, query:str) -> dict:
		result = self.get_from_cache(query)
		if result:
			return result
		result = 	requests.get(self.url + "search", {
		"sheets"   : "Item",
		"query"    : f'Name="{query}"',
		"language" : "en"
	}).json()
		self.add_to_cache(query, result)
		return result


	def find_key(self, data: dict, goal):
		for key, value in data.items():
			if key == goal:
				return data.get(key, None)
			if isinstance(value, dict):
				result = self.find_key(value, goal)
				if result :
					return result
			if isinstance(value, list):
				for item in value:
					if isinstance(item, dict) :
						result = self.find_key(item, goal)
						if result :
							return result
		return None


	def add_to_cache(self, item_name: str, data: dict):
		# This function should add the item_id to a cache.
		# For now, it will do nothing as a placeholder.


		if not os.path.exists('data/cache.json'):
			with open('data/cache.json', 'w') as f:
				json.dump({item_name: data}, f, indent=4)
				return
		with open('data/cache.json', 'r') as f :
			cache = json.load(f)
		cache[item_name] = data
		with open('data/cache.json', 'w') as f:
			json.dump(cache, f, indent=4)


	def get_from_cache(self, item_name: str):
		# This function should retrieve the item_id from a cache if it exists.
		# For now, it will return None as a placeholder.
		if not os.path.exists('data/cache.json') :
			return None
		with open('data/cache.json', 'r') as f:
			cache = json.load(f)
			return cache.get(item_name, None)






	def get_item_id(self, item):
		return self.find_key(self.search(item), "row_id")