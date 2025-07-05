import requests


class Universalis() :
	url = "https://universalis.app/api/v2/"

	def get_listings(self, item_id: int, world: str, amount: int = 50) :
		return requests.get(self.url + "/" + world + "/" + str(item_id), {
			'listings' : amount,
			'fields'   : 'listings'
		},
    headers={
      'User-Agent' : "Alices Shopping List"
    }
    ).json().get('listings', None)

