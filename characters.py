from random import randint
import names

## PLAYER GENERATION ##
class Player(object):

	def __init__(self):
		self.pl_name = None
		self.pl_stats = {"cont":randint(30,50),
    					"alc":randint(20,40)}
	
		
	def player_name(self):
	
		print "Enter your name"
		your_name = raw_input("> ")
    	self.pl_name = your_name



## CHARACTER GENERATION ##
class Character(object):

	def __init__(self):
		self.ch_name = None
		self.ch_stats = []
		
	def character_name(self):
		
		gender = randint(1,2)
		if gender == 1:
			gender = 'Male'
		elif gender == 2:
			gender = 'Female'
		
		self.ch_name = names.get_full_name(gender)
		
	def ch_stats(self):
		pass
		
		