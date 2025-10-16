import random

class Ai:
    def play(self):
        return 0

class Randomizer(Ai):
    def play(self):
        return random.randint(0,1)