class Character(object):
	
	def __init__(self):
		
		self.values = {}
		
		
	def insert_values(self):
		
		values = self.values
		
		values = {"hip":"hop",
					"foo":"bar"
					}
					
		return values
					
character = Character()
print character.insert_values()