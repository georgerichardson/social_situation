import characters as chars

# class Map(object):
# 
# 	rooms = {
# 			"kitchen":Kitchen(),
# 			"sofas":Sofas(),
# 			"dancefloor":Dancefloor(),
# 			"hallway":Hallway(),
# 			"garden":Garden()
# 			}
# 	
# 	def open_room(self):
# 		
# 		pass
		

class Engine(object):
	def __init__(self, player, characters):
		self.player = chars.Player()
		self.ply_name = self.player.ply_name()
		self.characters = []
	
	def the_time(self):
	
		pass
		
	def generate(self):
		character = chars.Character()
		self.characters.append(character)
		return character
		
#	def choose_room(self):
#		pass

	def play(self):
		ply_stats = self.player.ply_stats
		while ply_stats("cont") > 0 && ply_stats("alc") < 90:
		
		
class Interaction(object):
		
	def __init__(self, player, character):
		self.player = player
		self.ply_stats = player.ply_stats
		self.ch_name = character.ch_name		
		
	def meeting(self):
		greetings = ["You stand around sheepishly and accidentally make eye contact with someone a few feet away. They take this as a signal for engagement and turn towards you with an outstretched hand to shake. \"Hi, I\'m %s!\", they say as you shake hands." % self.ch_name,
					"You stand by a table and stare into space imagining all the useful things you could be getting on with. Just as you begin to yawn, someone introduces themself to you. \"Hi, I'm %s\", they say. You try to stifle the yawn to respond," % self.ch_name
					]
		print greetings[random.randint(0, len(greetings)-1)]
	
	def talk(self):
		confirmations = ["You stay to chat with %s." % self.ch_name]
		print confirmations[random.randint(0, len(confirmations)-1)]
	
	def run_away(self):
		excuses = ["You look into a different part of the room and wave. \"Sorry, I just have to say hi to my friend\", you lie. \"I'll be back over in a minutes\", you lie again as you march off to an empty part of the party."
					]
		
	def outcomes(self):
		
		
	def next_move(self):
		pass
	
	def drink(self):
		drink = raw_input("Would you like a drink? (y/n): ")
		if drink == "y":
			print "You pick up another beer and begin to sip it down."
			self.player.ply_stats['alc'] += 10
			if 75 > self.ply_stats['alc'] > 0:
				self.ply_stats['cont'] = (10.0/75.0) * self.ply_stats['alc']
			
		elif drink == "n"
			print "You decide to hold out a bit longer for another drink. Maybe you can make it through the night."
	
	def interact(self):
		
	
	
