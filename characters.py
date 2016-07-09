from random import randint
import names

#######################
## PLAYER GENERATION ##
#######################

# Class for the player
class Player(object):
	# initialise player name and stats including contentment and alcohol level
	def __init__(self):
		self.ply_stats = {"cont":randint(30,50),
    					"alc":randint(20,40)
    					}
		self.player_name()
	
	# allow the user to enter their own name
	def player_name(self):
	
		print "Enter your name"
		your_name = raw_input("> ")
		self.ply_name = your_name
		
	def __str__(self):
		print self.ply_name
		print self.ply_stats("alc")


#####################		
## CHARACTERISTICS ##		
#####################

class Characteristic(object):

	def __init__(self, ch_name, ply_name):
		pass

## POSITIVE CHARACTERISTICS ##		
class Similarity(Characteristic):
	def __init__(self, ch_name, ply_name):
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
					
		hobby = niche_adj[randint(0, len(niche_adj) -1)] +  niche_noun[randint(0, len(niche_noun) -1)]
		
		return hobby
	
	def intro1(self):
		ch_name = self.ch_name
		ply_name = self.ply_name
		hobby = self.shared_hobby()
		self.stat_change = self.stat_change()		
		
		intro = ["Minutes have passed and your eyes are beginning to glaze over when suddenly your ears prick up as %s casually mentions \"%s\". You can't believe your luck, winding up talking to someone who shares the same interest as you! The minutes pass swiftly as you share experiences, tips and plans." % (ch_name, hobby),
		"You struggle to initiate all but the most boring small talk with %s whose eyes begin to wander around the room. They quickly focus back on you when you recall a story about the time you were researching for your book on %s. \"I can't believe there's someone else here into that\" they exclaim and the pair of you launch into a heated debate on the intricaces of your shared passion." % (ch_name, hobby)]
		
		return intro[randint(0, len(intro)-1)]
				
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
	def __init__(self, ch_name, ply_name):
		self.ch_name = ch_name
		self.ply_name = ply_name
		self.stat_change = self.stat_change()
			
	def __str__(self):
		return "Interesting"
			
	def intro1(self):
		ch_name = self.ch_name
		ply_name = self.ply_name
		
		intro = ["%s is well travelled and the two of you chat easily about your train travels around Europe. Maybe this isn't so bad after all." % ch_name,
		"After a hesitant start, you and %s get chatting about topical current affairs, finding that you have share some common views. A good shared rant makes you feel slightly better about having been dragged here." % ch_name]
		
		return intro[randint(0, len(intro)-1)]
	
	def stat_change(self):
		cont_chg = 20
		return cont_chg

## NEGATIVE CHARACTERISTICS ##	
class SelfCentered(Characteristic):
	def __init__(self, ch_name, ply_name):
		self.ch_name = ch_name
		self.ply_name = ply_name
		self.stat_change = self.stat_change()
	
	def __str__(self):
		return "SelfCentred"
			
	def intro1(self):
		ch_name = self.ch_name
		ply_name = self.ply_name
		
		intro = ["%s seems OK at first, even laughing at your joke about frozen mint. However the conversation quickly moves onto their workout regime. Half an hour later and you're still talking about %s\'s calorie intake, mid term targets and their perfected meal replacement mix. You might as well be a brick wall." % (ch_name, ch_name),
		"It's been 20 minutes and all you have talked about is %s. You've heard about the inconvenience of scheduling their weekly hairdresser appointments around their dog's busy social life and the trouble they're having with their next door neighbour complaining about their voyeuristic sex life. This isn't what you signed up for." % ch_name]
		
		return intro[randint(0, len(intro)-1)]
				
	def stat_change(self):
		cont_chg = -20
		return cont_chg

	
class KnowItAll(Characteristic):
	def __init__(self, ch_name, ply_name):
		self.ch_name = ch_name
		self.ply_name = ply_name
		self.stat_change = self.stat_change()
	
	def __str__(self):
		return "KnowItAll"
			
	def intro1(self):
		ch_name = self.ch_name
		ply_name = self.ply_name
		
		intro = ["%s asks inquisitively about your job. \"Oh right. Done a bit of that myself.\" they say casually. You spend an hour being lectured to about your own profession by someone who has clearly read a few hobbyist magazines back in 2003."  % ch_name,
		"You mention your job in passing and %s latches on, beginning to interject their opinion at every opportunity. Despite having little to no experience in your field, %s tells you with great authority about the issues with your line of work what they think you should do about them." % (ch_name, ch_name)]
		
		return intro[randint(0, len(intro)-1)]
				
	def stat_change(self):
		cont_chg = -20
		return cont_chg

	
class Awkward(Characteristic):
	def __init__(self, ch_name, ply_name):
		self.ch_name = ch_name
		self.ply_name = ply_name
		self.stat_change = self.stat_change()
	
	def __str__(self):
		return "Awkward"
			
	def intro1(self):
		ch_name = self.ch_name
		ply_name = self.ply_name
		
		intro = ["It turns out you share some interests and taste in music with %s and start to chat easily, but the conversation is stilted. Eventually it dries up and you find that you're both folding your arms and looking around the party. %s gets out their phone and starts to look at cat photos."  % (ch_name, ch_name),
		"%s seems quiet, but that's ok. You try to strike up conversation by asking a few of the usual questions. %s responds monosyllabically and fails to reciprocate. You're trapped in a conversational desert and start to look desperately around the room." % (ch_name, ch_name)]
		
		return intro[randint(0, len(intro)-1)]
				
	def stat_change(self):
		cont_chg = -20
		return cont_chg


class Drunk(Characteristic):
	def __init__(self, ch_name, ply_name):
		self.ch_name = ch_name
		self.ply_name = ply_name
		self.stat_change = self.stat_change()
	
	def __str__(self):
		return "Drunk"
			
	def intro1(self):
		ch_name = self.ch_name
		ply_name = self.ply_name
		
		intro = ["At first, %s seems interested in what you're talking about, but gradually you realise that their stare is vacant and they're just grinning, trying to nod at appropriate moments and not throw up. They've got no idea what you're talking about."  % ch_name,
		"Immediately, you realise your mistake. %s is tightly gripping their glass and swaying on the spot. You attempt to steady them, but they stagger forward and spill their drink on your shoes. They straighten up, apologise and start to tell you how great you are while tightly gripping your wrist." % ch_name]
		
		return intro[randint(0, len(intro)-1)]
				
	def stat_change(self):
		cont_chg = -20
		return cont_chg
	
class Boring(Characteristic):
	def __init__(self, ch_name, ply_name):
		self.ch_name = ch_name
		self.ply_name = ply_name
		self.stat_change = self.stat_change()
	
	def __str__(self):
		return "Boring"
			
	def intro1(self):
		ch_name = self.ch_name
		ply_name = self.ply_name
		
		intro = ["Mere seconds pass before you realise your fatal mistake. %s\'s dullness hits you like a heatwave. How could someone possibly have so much to say about the quality of the road surfaces near their house? Time grinds to an excruciatingly slow pace and you enter into a trance like state." % ch_name,
		"Despite just meeting you, %s has whipped out their phone to show you some \"funny videos\". You stand there forcing a twisted polite smile as %s laughs on cue at every eagerly anticipated and apparently hilarious moment. You begin to despair for humanity as well as yourself." % (ch_name, ch_name)]
		
		print intro[randint(0, len(intro)-1)]
				
	def stat_change(self):
		return -20


##########################
## CHARACTER GENERATION ##
##########################

# class for characters that are encountered in the game
class Character(object):
	
	# list of all possible characteristics

	
	# number of possible characteristics					
	no_characteristics = 1
	
	# initialise placeholders for character name and characteristics
	def __init__(self):
		self.all_characteristics = [Similarity(ch_name = None, ply_name = None),
						Interesting(ch_name = None, ply_name = None),
						SelfCentered(ch_name = None, ply_name = None),
						KnowItAll(ch_name = None, ply_name = None),
						Awkward(ch_name = None, ply_name = None),
						Drunk(ch_name = None, ply_name = None),
						Boring(ch_name = None, ply_name = None)
						]
		self.ch_name = self.ch_name()
		self.ch_stats = self.ch_characteristics()

		
		
	# randomly assign gender and generate a character name 	
	def ch_name(self):
		
		gender = randint(1,2)
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
		choices = list(self.all_characteristics)		
		# loop through allowed number of characteristics and randomly select from "choices"
		for i in xrange(self.no_characteristics):
			ch_id = randint(0,len(choices)-1)
			ch_stats.append(choices[ch_id])
			del choices[ch_id]
			
		return ch_stats
			
	def meeting(self, ply_name):
		ch_reveal = self.ch_stats[randint(0,len(self.ch_stats)-1)]
		ch_reveal.ch_name = self.ch_name
		ch_reveal.ply_name = ply_name
		print ch_reveal.intro1()		
		i = ch_reveal.stat_change
		return i
		