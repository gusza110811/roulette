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

class CarefulGambler(Ai):
    def __init__(self, live_rounds=1):
        self.total_chambers = 6
        self.total_live = live_rounds
        self.shots_fired = 0
        self.estimated_live = live_rounds

    def play(self, player_plays):
        self.shots_fired += player_plays
        remaining_chambers = self.total_chambers - self.shots_fired
        if remaining_chambers <= 0:
            remaining_chambers = 1

        p_live = self.estimated_live / remaining_chambers
        p_blank = 1 - p_live

        # More agressive over time
        threshold = 0.5 - (self.shots_fired * 0.05)

        if p_blank > threshold:
            choice = 0
        else:
            choice = 1

        self.shots_fired += 1
        self.estimated_live = max(0.1, self.estimated_live * 0.95)

        return choice