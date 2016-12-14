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
	# is called a "constructor" in other languages and this will not work without it.
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