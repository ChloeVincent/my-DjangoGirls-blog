import pykew.ipni as ipni

class Species():
	"""docstring for Species"""
	name = ""
	count= 0


	def __init__(self, name):
		self.name = name
		
		result = ipni.search(name)
		self.count= result.size()
