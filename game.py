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
	# The variable for any number of objects?  Init is still confusing, but I know it's important and
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



class BritishCamp(Scene):

    def enter(self):
    	#Put in storyline/text here to intro scene
        code = "%d" % (randint(1,5))
        guess = raw_input ("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 2:
            print #Witty response for messing up code
            guesses += 1
            guess = raw_input("[keypad]> ")

        if guess == code:
            #put in storyline here for winning the game
            return 'country_saved'
        else:
            print #story for failure to win the game
            return 'awake'

#Put in finishing/winning response

class Map(object):

    scenes = {
        "opening_scene": OpeningScene(),
        "british_camp": BritishCamp(),
        "awake": Awake(),
        "country_saved"
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('opening_scene')
a_game = Engine(a_map)
a_game.play()
