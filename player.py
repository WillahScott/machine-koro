from typing import Dict
from dataclasses import dataclass

from cards import Card


@dataclass
class Player(object):
    name: str
    money: int
    blue_cards: Dict[Card]
    def __init__(self, money) -> None:
        self.money = money