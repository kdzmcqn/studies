from sys import exit
from random import randint
from textwrap import dedent


class Scene(object):

    def enter(self):
        print("This scene is not yat configured.")
        print("Subclass it and implement enter().")
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

        # be sure to print out the last scene
        current_scene.enter()


class Death(Scene):

    quips = [
        "You died. You kinda suck at this.",
        "Your Mom would be proud...if she were smarter.",
        "Such a looser.",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips) - 1)])
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
        some story
        na
        mahaba
        super
        """))

        action = input("> ")

        if action == "shoot!":
            print(dedent("""
            stuff na nangyari
            """))
            return 'death'

        elif action == "dodge!":
            print(dedent("""
            stuff na nangyari
            """))
            return 'death'

        elif action == "tell a joke":
            print(dedent("""
            jokes
            """))
            return 'laser_weapon_armory'

        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
        super laser weapon
        """))

        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        print(code)
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZZD!" + '*' * (guesses + 1))
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
            open
            """))
            return 'the_bridge'
        else:
            print(dedent("""
            wew
            """))
            return 'death'


class TheBridge(Scene):

    def enter(self):
        print(dedent("""
        You burst onto the Bridge with the netron destruct bomb
        under your arm and surprise 5 Gothons who are trying to
        take control of the ship. Each of them has an even uglier
        clown costume than the last. They haven't pulled their
        weapons out yet, as they see the active bomb under your
        arm and don't want to set it off.
        """))

        action = input("> ")

        if action == "throw the bomb":
            print(dedent("""
            In a panic you throw the bomb at the group of Gothons
            and make a leap for the door. Right as you drop it a
            Gothon shoots you right in the back killing you. As
            you die you see another Gothon frantically try to
            disarm the bomb. You die knowing they will probably
            blow up when it goes off.
            """))
            return 'death'

        elif action == "slowly place the bomb":
            print(dedent("""
            You point your blaster at the bomb under your arm and
            the Gothons put their hands up and start to sweat.
            You inch backward to the door, open it, and then
            carefully place the bomb on the floor, pointing your
            blaster at it. You then jump back through the door,
            punch the close button and blast the lock so the
            Gothons can't get out. Now that the bomb is placed
            you run to the escape pod to get off this tin can.
            """))

            return 'escape_pod'
        else:
            print("DOES NOT COMPUTE!")
            return 'the_bridge'


class EscapePod(Scene):

    def enter(self):
        print(dedent("""
        You rush through the ship desperately trying to make it to
        the escape pod before the whole ship explodes. It seems
        like hardly any Gothons are on the ship, so your run is
        clear of interference. You get to the chamber with the
        escape pods, and now need to pick one to take. Some of
        them could be damaged but you don't have time to look.
        There's 5 pods, which one do you take?
        """))

        good_pod = randint(1, 5)
        print(good_pod)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(dedent(f"""
            {guess}
            """))
            return 'death'
        else:
            print(dedent(f"""
            {guess}
            """))
            return 'finished'


class Finished(Scene):

    def enter(self):
        print("You won! Good job.")
        return 'finished'


class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished()
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
