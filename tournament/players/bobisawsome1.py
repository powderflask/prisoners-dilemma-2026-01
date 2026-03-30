# Auto-generated from GitHub Issue submission
# Author: bobisawsome1
# Generated: 2026-03-30T19:39:11.770509+00:00Z

# Imports for building your Player
from axelrod import Player, Action
import random

class LebronJames(Player):
    """List the names of all students who worked on this class here. """
    name = "Lebron James"

    def strategy(self, opponent):
        """ This example is the Cooperator strategy: always cooperate. """
        match_history = zip(self.history, opponent.history)
        C_count = 0
        D_count = 0

        for s, o in match_history:
          if o == Action.C:
            if s == Action.D:
              D_count +=1

            else:
              C_count += 1

          elif o == Action.D:
            if s == Action.C:
              D_count += 1

        if D_count >= C_count:
          return Action.D

        else:
          return Action.C


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
