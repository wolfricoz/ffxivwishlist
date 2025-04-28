import requests


class xivapi():
	url = "https://v2.xivapi.com/api/"
	# TODO: Add a cache for this function, it's not very efficient to call this every time - the data doesn't change that often.
	def search(self, query:str) -> dict:
		return	requests.get(self.url + "search", {
		"sheets"   : "Item",
		"query"    : f'Name="{query}"',
		"language" : "en"
	}).json()


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


	def get_item_id(self, item):
		return self.find_key(self.search(item), "row_id")