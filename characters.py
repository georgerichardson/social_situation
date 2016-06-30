from random import randint
import names

## PLAYER GENERATION ##
# Class for the player
class Player(object):
	# initialise player name and stats including contentment and alcohol level
	def __init__(self):
		self.ply_name = None
		self.ply_stats = {"cont":random.randint(30,50),
    					"alc":random.randint(20,40)}
	
	# allow the user to enter their own name
	def player_name(self):
	
		print "Enter your name"
		your_name = raw_input("> ")
		self.ply_name = your_name



## CHARACTER GENERATION ##
# class for characters that are encountered in the game
class Character(object):
	
	# list of all possible characteristics
	all_characteristics = [Similarity(),
						Interesting(),
						SelfCentered(),
						KnowItAll(),
						Awkward(),
						Drunk(),
						Nosey(),
						StoryTopper()]
	
	# number of possible characteristics					
	no_characteristics = 2
	
	# initialise placeholders for character name and characteristics
	def __init__(self):
		self.ch_name = self.ch_name()
		self.ch_stats = self.ch_characteristics()
		
		
	# randomly assign gender and generate a character name 	
	def ch_name(self):
		
		gender = random.randint(1,2)
		if gender == 1:
			gender = 'Male'
		elif gender == 2:
			gender = 'Female'
		# use "names" package to generate character's name 
		ch_name = names.get_first_name(gender)
		
		return ch_name
	
	# choose characteristics for character
	def ch_characteristics(self):
		
		ch_stats = []
		choices = list(all_characteristics)		
		# loop through allowed number of characteristics and randomly select from "choices"
		for i in xrange(no_characteristics):
			ch_id = randint(0,len(choices)-1)
			ch_stats.append(choices[ch_id])
			del choices[ch_id]
			
		return ch_stats
			


## CHARACTERISTIC PARENT ##		
class Characteristic(object):

	def __init__(self, ch_name, ply_name):
		pass

## POSITIVE CHARACTERISTICS ##		
class Similarity(Characteristic):
	def __init__(self, ch_name, ply_name)
		self.ch_name = ch_name
		self.ply_name = ply_name
	
	def __str__(self):
		return "Similarity"
	
	def shared_hobby(self):
		niche_adj = ["retro ",
					"European ",
					"1970s ",
					"early 20th century ",
					"artesanal ",
					"digital ",
					"ceramic ",
					"fantasy "]
		
		niche_noun = ["modular synthesisers",
					"bird watching",
					"train spotting",
					"watch collecting",
					"anchovy farming",
					"flower arranging",
					"gravy recipes",
					"duct tape art",
					"model rocketeering",
					"walnut decorating"]
					
		hobby = niche_adj[random.randint(0, len(niche_adj -1)] +  niche_noun[random.randint(0, len(niche_noun -1)]
		
		return hobby
	
	def intro1(self):
		ch_name = self.ch_name
		ply_name = self.ply_name
		hobby = self.shared_hobby()
		
		intro = ["Minutes have passed and your eyes are beginning to glaze over when suddenly your ears prick up as %s casually mentions \"%s\". You can't believe your luck, winding up talking to someone who shares the same interest as you! The minutes pass swiftly as you share experiences, tips and plans." % (ch_name, hobby),
		"You struggle to initiate all but the most boring small talk with %s whose eyes begin to wander around the room. They quickly focus back on you when you recall a story about the time you were researching for your book on %s. \"I can't believe there's someone else here into that\" they exclaim and the pair of you launch into a heated debate on the intricaces of your shared passion." % (ch_name, hobby)]
		
		return intro[random.randint(0, len(intro)-1)]
				
	def stat_change(self):
		cont_chg = 20
		return cont_chg
					
# 	def intro2(self):
# 		pass
# 	
# 	def ply_stay(self) 
# 		ch_name = self.ch_name
# 		ply_name = self.ply_name
# 		hobby = self.shared_hobby()	
# 	
# 		stay = ["By this point, you're having a moderately good time and decide to hang around for a bit longer"
# 	
# 	ply_excuse = []
	

	
class Interesting(Characteristic):
	pass

## NEGATIVE CHARACTERISTICS ##	
class SelfCentred(Characteristic):
	pass
	
class KnowItAll(Characteristic):
	pass
	
class Awkward(Characteristic):
	pass

class Drunk(Characteristic):
	pass
	
class Nosey(Characteristic):
	pass

class StoryTopper(Characteristic):
	pass
		
		