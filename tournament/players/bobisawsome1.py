# Auto-generated from GitHub Issue submission
# Author: bobisawsome1
# Generated: 2026-03-30T19:23:55.774678+00:00Z

# Imports for building your Player
from axelrod import Player, Action

class ChuckNorris(Player):
    """List the names of all students who worked on this class here. """
    name = "Chuck Norris(RIP)"

    def strategy(self, opponent):
        """ This example is the Cooperator strategy: always cooperate. """
        opp_history = opponent.history
        opp_Cs = 0
        for action in opp_history:
          if action == Action.C:
            opp_Cs += 1

        self_history = self.history
        self

        if len(opp_history) == 0:
          return Action.D

        elif (opp_Cs / len(opp_history)) > 0.70:
          return Action.C

        else:
          return Action.D
