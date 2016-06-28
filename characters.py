from random import randint
import names

## PLAYER GENERATION ##
# Class for the player
class Player(object):
	# initialise player name and stats including contentment and alcohol level
	def __init__(self):
		self.pl_name = None
		self.pl_stats = {"cont":random.randint(30,50),
    					"alc":random.randint(20,40)}
	
	# allow the user to enter their own name
	def player_name(self):
	
		print "Enter your name"
		your_name = raw_input("> ")
		self.pl_name = your_name



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
		self.ch_name = None
		self.ch_stats = []
		
	# randomly assign gender and generate a character name 	
	def character_name(self):
		
		gender = random.randint(1,2)
		if gender == 1:
			gender = 'Male'
		elif gender == 2:
			gender = 'Female'
		# use "names" package to generate character's name 
		self.ch_name = names.get_full_name(gender)
	
	# choose characteristics for character	
	def ch_characteristics(self):
		
		choices = list(all_characteristics)		
		# loop through allowed number of characteristics and randomly select from "choices"
		for i in xrange(no_characteristics):
			ch_id = randint(0,len(choices)-1)
			self.ch_stats.append(choices[ch_id])
			del choices[ch_id]


## CHARACTERISTIC PARENT ##		
class Characteristic(object):

	def __init__(self):
		pass

## POSITIVE CHARACTERISTICS ##		
class Similarity(Characteristic):
	pass
	
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
		
		