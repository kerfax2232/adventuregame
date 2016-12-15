#Imports exit variable (is variable right phrase?) from sys module.  This will allow for exit from Python
from sys import exit
#Imports randint (random integer) from random module.  This will allow for random integer generation for guessing numbers later
from random import randint

#This is a class to callback to in later parts of the game
class Scene(object):

    def enter(self):
        exit(1)

class Engine(object):

	#Still unclear on __init__ and self in terms of importance.  Self I believe allows you to call
	# The variable for any number of objects?  Also is 
	# implied argument often.  Init is still confusing, but I know it's important and
	# is called a "constructor" in other languages (Stack Overflow)  and this will not work without it.
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
    	# This will start the game with the opening scene
        current_scene = self.scene_map.opening_scene()
        #This determines the last scene
        last_scene = self.scene_map.next_scene('finished')

        # Saying while scene is not the last scene, go to next scene
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

class Awake(Scene):

	#This is a list of attempted witty sayings
    pun = [
        "You could have done so much better -- if you only had a brain",
         "Next time do the same thing.  But better",
         "Thanks for losing the war.  America will have to wait for the next revolution until it becomes great again",
         "Well, at least you can go back to playing Pokemon Go!"
    ]

    def enter(self):
    	# Since starting point is 0, -1 is added to only allow for puns 
        print Awake.pun[randint(0, len(self.pun)-1)]
        exit(1)

class OpeningScene(Scene):

    def enter(self):
        f = open("opening_scene.txt")
        print(f.read())

        action = raw_input("> ")

        if action == "canadian":
        	opening_scene_negative = open("opening_scene_resp_negative.txt")
        	print(opening_scene_negative.read())
        	return 'british_camp'

        elif action == "sleep":
    		opening_scene_negative = open("opening_scene_resp_negative.txt")
    		print(opening_scene_negative.read())
    		return 'british_camp'

        elif action == "i'm in":
			opening_scene_positive = open("opening_scene_resp_negative.txt")
			print(opening_scene_positive.read())
			return 'british_camp'

		#Without else traceback error is thrown with wrong answer
        else:
			print "Please use American English. (And check that everything is in lowecase!)"
			return 'opening_scene'



class BritishCamp(Scene):

    def enter(self):
    	british_intro = open("british_camp_intro.txt")
    	print(british_intro.read())
        password = "%d" % (randint(1,5))
        guess = raw_input ("What is your guess? > ")
        guesses = 0

        #Saying while guess is under this amount of guesses, print/do this
        while guess != password and guesses < 5:
            print '"Try again lad/lass."  The general and his guards begin to encircle you, wary of your true identity'  
            guesses += 1
            guess = raw_input("What is your guess?> ")

        #If guess is correct
        if guess == password:
            print '"We\'ve been waiting for you!  However, we don\'t actually have the map.  Go further into the camp.'
            print 'You\'ll have to solve a math problem for them to get the map of troop movements"'
            return 'obtaining_map '
        
        #If guess is wrong after specified amount of guesses
        else:
            print #story for failure to win the game
            return 'awake'

class ObtainingMap(Scene):
	def enter(self):
		num1 = randint(0,10)
		num2 = randint(0,10)
		ans = num1+num2
		guesses = 0
		print "Try to answer this:"
		print(num1,"+", num2)
		player_answer = int(input("What's the answer?"))
		while player_answer != ans and guesses < 2:
			print "Try again lad/lass.  Although if you can't answer basic maths I wonder if you can read this map."
			guesses += 1
			player_answer = int(input("What's the answer?"))

		if player_answer == ans:
			print "Here\'s your map!  God Save the King!"
			#return 'country_saved'

		else:
			print "You've failed at obtaining the map.  However, you didn't fail at playing this game, and isn't that what's important?"
			return 'awake'

#Put in finishing/winning response

# Class defines the scene names, changing scenes, etc
class Map(object):

    scenes = {
    	#remember to put the comma at the end genius
        "opening_scene": OpeningScene(),
        "british_camp": BritishCamp(),
        "obtaining_map": ObtainingMap(),
        "awake": Awake(),
        #"country_saved": CountrySaved(),
    }


    def __init__(self, start_scene):
        self.start_scene = start_scene

    # sends scene to next specified scene by tying next_scene to getting next scene name
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    #defines opening scene    
    def opening_scene(self):
        return self.next_scene(self.start_scene)

#Starts game at opening scene
a_map = Map('opening_scene')
# ties game.play to the 
a_game = Engine(a_map)
a_game.play()
