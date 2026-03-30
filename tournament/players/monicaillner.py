# Auto-generated from GitHub Issue submission
# Author: monicaillner
# Generated: 2026-03-30T19:38:29.282033+00:00Z

# Imports for building your Player
from axelrod import Player, Action

class SuperPunisher(Player):
    """List the names of all students who worked on this class here. """
    name = "Super Punisher"

    def strategy(self, opponent):
        """ Cooperates until other player defects, then defects once. """
        try:      
          if opponent.history[-1] == Action.D:    # checks history - if previously opponent deflected
            return Action.D

        except IndexError:    # for no history, starts with cooperating
          return Action.C

        else:           # if opponent previously cooperated
          return Action.D
