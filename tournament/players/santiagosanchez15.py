# Auto-generated from GitHub Issue submission
# Author: santiagosanchez15
# Generated: 2026-03-30T19:16:55.566567+00:00Z

from axelrod import Player, Action

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
