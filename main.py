from enum import Enum
import random
from collections import deque
import time
from ai import *

class Round(Enum):
    LIVE=True
    BLANK=False

class state(Enum):
    NONE=-1
    GOING=0
    LOST=1
    WIN=2

CLEAR = "\033[2J\033[H"
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
GRAY = "\033[90m"
RESET = "\033[0m"

class Game:
    def __init__(self,live_rounds:int,ai:Ai = Randomizer):
        self.live_rounds = live_rounds
        self.state = state.NONE
        self.ai:Ai = ai(live_rounds) # literally the most basic ai

        self.player_blank_count = 0

    def ai_turn(self):
        chamber = self.barrel.popleft(); self.barrel.append(chamber)
        choice = self.ai.play(self.player_blank_count)
        if choice == 0:
            print("The opponent chose to shoot themself\n")
            if chamber == Round.BLANK:
                print(BLUE+"It was blank, they get another turn..."+RESET)
                time.sleep(1)
                self.ai_turn()
            else:
                print(GREEN +"It was a live round, you won"+RESET)
                self.state = state.WIN
        else:
            print("The opponent chose to shoot you\n")
            time.sleep(2)
            if chamber == Round.BLANK:
                print(GRAY+"It was blank, the game continues"+RESET)
                time.sleep(1)
            else:
                print(RED +"It was a live round, you died"+RESET)
                self.state = state.LOST
        self.player_blank_count = 0

    def player(self):
        print("Choose an action\n\
1. Shoot yourself\n\
2. Shoot the opponent")
        choice = None
        while not(choice == "1" or choice == "2"):
            choice = input(">")
        chamber = self.barrel.popleft(); self.barrel.append(chamber)
        if chamber == Round.BLANK:
            if choice == "1":
                time.sleep(0.5+random.random())
                print(BLUE+"It was blank, you get to play another turn"+RESET)
                time.sleep(1)
                self.player_blank_count += 1
                self.player()
            else:
                print(GRAY+"It was blank, the game continues"+RESET)
                time.sleep(1)
        elif chamber == Round.LIVE:
            if choice == "1":
                time.sleep(1)
                print(RED+"It was a live round, you are dead."+RESET)
                self.state = state.LOST
            elif choice == "2":
                print(GREEN+"It was a live round, you have won."+RESET)
                self.state = state.WIN
    
    def game(self):
        print(CLEAR)
        print(f"Russian Roulette, {self.live_rounds} live, {6-self.live_rounds} blank")
        self.barrel = deque([Round.BLANK] * (6-self.live_rounds) + [Round.LIVE]*self.live_rounds)
        random.shuffle(self.barrel)

        self.state = state.GOING

        while self.state == state.GOING:
            self.player()
            if self.state == state.GOING:
                self.ai_turn()
        return self.state

if __name__ == "__main__":
    game = Game(1,Coward)
    game.game()