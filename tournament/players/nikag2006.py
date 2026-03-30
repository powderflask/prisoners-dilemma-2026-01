# Auto-generated from GitHub Issue submission
# Author: nikag2006
# Generated: 2026-03-30T20:41:20.569887+00:00Z

from axelrod import Player, Action

class NikaG(Player):
    """List the names of all students who worked on this class here. """
    name = "NikaG"

    def strategy(self, opponent):
        # In the first move, just cooperate
        if not opponent.history:
            return Action.C
        
        # Otherwise, do what the opponent did on their last move
        last_opponent_move = opponent.history[-1]
        return last_opponent_move
