# Auto-generated from GitHub Issue submission
# Author: peterspitz
# Generated: 2026-03-30T19:17:09.043559+00:00Z

# Imports for building your Player
from axelrod import Player, Action

class Peter_Spitz(Player):
    """List the names of all students who worked on this class here. """
    name = "Peter_Spitz"

    def strategy(self, opponent):
        """ This example is the Cooperator strategy: always cooperate. """

        test_1 = len([x for x in opponent.history if x == Action.C])
        test_2 = len(opponent.history)

        if test_2 == 0:
          return Action.C
        elif test_1/test_2 > .75 and opponent.history[-1] == Action.C:
          return Action.C
        else:
          return Action.D
