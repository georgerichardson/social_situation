import characters as chars

class Map(object):

	rooms = {
			"kitchen":Kitchen(),
			"sofas":Sofas(),
			"dancefloor":Dancefloor(),
			"hallway":Hallway(),
			"garden":Garden()
			}
	
	def open_room(self):
		
		pass
		

class Engine(object):
	def __init__(self, player, characters):
		self.player = chars.Player()
		self.ply_name = self.player.ply_name()
	
	def the_time(self):
	
		pass
	
#	def choose_room(self):
#		pass

	def play(self):
	
		pass
		
		
class Interaction(object):
		
	def __init__(self, player, character):
		self.player = player
		self.characters = []
		
	def generate(self):
		character = chars.Character()
		self.characters.append(character)		
		
	def meeting(self, ply_name, ch_name):
		greetings = ["You stand around sheepishly and accidentally make eye contact with someone a few feet away. They take this as a signal for engagement and turn towards you with an outstretched hand to shake. \"Hi, I\'m %s!\", they say as you shake hands." % ch_name,
					"You stand by a table and stare into space imagining all the useful things you could be getting on with. As you reach up to stifle a yawn, you elbow the person next to you. 
	
	def talk(self):
		pass
	
	def run_away(self):
		pass
		
	def outcomes(self):
		pass
		
	def next_move(self):
		pass
	
	def drink(self):
		pass
	
	def interact(self):
		pass
	
	
