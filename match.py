import random
from typing import Tuple

def roll_dice(num_dice=1) -> Tuple[int, bool]:
    """Rolls dice, returns sum of values and if it was
     a doubles roll (only applies for num_dice=2)"""
    # return sum([ random.randint(1,6) for _ in num_dice ])
    d1 = random.randint(1,6)
    if num_dice == 2:
        d2 = random.randint(1,6)
        return (d1+d2, d1==d2)
    return (d1, False)


def init_match(num_players: int):
    board = {

    }
    players = [
        {
            "money": 3,
            "blue_cards": [],
            "green_cards": [],
            "red_cards": [],
            "purple_cards": [],
        } for _ in range(num_players)
    ]

def play_match():
    board = {}


if __name__ == "__main__":
    play_match()