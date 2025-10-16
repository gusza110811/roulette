import random

class Ai:
    def __init__(self,live_count):
        self.live_count = live_count
    def play(self, player_plays):
        # return 0 => shoot self
        # return 1 => shoot opponent
        return 0

class Randomizer(Ai):
    def play(self,_):
        return random.randint(0,1)

class Coward(Ai):
    def __init__(self, live_rounds=1):
        self.total_live = live_rounds
        self.shots_fired = 0
        self.live = live_rounds

    def play(self, player_plays):
        self.shots_fired += player_plays

        remaining = 6-self.shots_fired
        chance = self.live/remaining
        if chance < (1/4):
            choice = 0
        else:
            choice = 1

        self.shots_fired += 1
        return choice