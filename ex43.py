from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "You have thunderously entered a room at full pace, you go semi prone and safely check out the room"
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        #be sure to print out the last scene_map
        current_scene.enter()

class Death(Scene):

    quips = [
            "\nYou died but you can still keep going! ... no just joking, you're completely dead",
            "\nMy grandma could survive longer than you, but she does jog everyday",
            "\nWhoa you just died?! I can't believe you survived that long",
            "\nMy uncle Geoffrey is better at this and he's only got 1 arm... and is a horse"]

    def enter(self):
        print Death.quips[randint(0,len(self.quips)-1)]
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print "\nBOOM! holy tomorrow, a scruffy looking nerfherder has just smashed open the door to your ship."
        print "The freak whips out a matte black glock in a flash like he was born in the wild wild west"
        print "Before he shoots, you sluggishly bring up your stone sundial wristwatch and twist it back making time go at 0.10 speed"
        print "This will only last for a few moments, but it gives you time to think. What do you do?"
        action = raw_input(">")

        if action == "shoot":
            print "\nYour hand goes to your waist to grab your gun."
            print "Before you even realise you only brought a spade, the shabby nerfherder blasts you with his glock"
            print "sending your face into oblivion."
            return 'death'
        if action == "run":
            print "\nYou breakdance backwards and a little to the left to"
            print "flip over a small bordie collie. This brings you into a new room"
            return "laserweaponarmory"
        else:
            print "\nYour fingers are fat"
            return 'central_corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
        print "A large hand grenade the size of a watermelon is sitting in front you"
        print "like a unwanted turtle. What do you do?"
        action = raw_input(">")

        if action == "move it":
            print "it explodes like an overly ripe fruit and covers you in a deliciouly lethal chemical gas"
            print "your body melts into a puddle and the nerfherder comes in with a bowl of chips and uses your remains as a spicy sauce."
            return "death"
        elif action == "jump":
            return 'finished'
        else:
            print "Your fingers are fat"
            return 'laserweaponarmory'

# class TheBridge(Scene):
#
#     def enter(self):
#         pass
#
# class EscapePod(Scene):
#
#     def enter(self):
#         pass

class Finished(Scene):

    def enter(self):
        print "You won! Good job."
        return 'finished'

class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laserweaponarmory': LaserWeaponArmory(),
        'finished': Finished(),
        "death": Death()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
