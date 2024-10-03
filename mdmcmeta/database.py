from schema import MetadataCreate

class Database:
	__data : dict = {}
	__last_id : int

	def store(self, obj):
		raise NotImplementedError
