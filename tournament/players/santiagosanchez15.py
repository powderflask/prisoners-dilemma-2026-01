# Auto-generated from GitHub Issue submission
# Author: santiagosanchez15
# Generated: 2026-03-30T19:37:42.045810+00:00Z

import random
from axelrod import Player, Action

class SneakyAggressor(Player):
    """ Authors: Sanchit and Santiago """
    name = "Sneaky Aggressor"

    def strategy(self, opponent: Player) -> Action:
        # Turn 1: Cooperate
        if not opponent.history:
            return Action.C

        # 10% chance to randomly backstab and steal 5 points
        if random.random() < 0.2:
            return Action.D

        # Otherwise, just copy their last move
        return opponent.history[-1]


class SmartAggressor(Player):
    """
    Authors: [Sanchit,Santiago / Team Ruthless]
    """
    name = "The Smart Aggressor"

    def strategy(self, opponent: Player) -> Action:
        # Strike first: Defect on the very first turn
        if not opponent.history:
            return Action.D

        # After turn 1, just copy whatever they did last
        return opponent.history[-1]
