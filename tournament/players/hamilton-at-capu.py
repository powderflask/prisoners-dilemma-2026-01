# Auto-generated from GitHub Issue submission
# Author: hamilton-at-capu
# Generated: 2026-01-06T18:40:17.775821+00:00Z

from axelrod import Player, Action

class ModeratePlayer(Player):
    """List the names of all students who worked on this class here. 
       Mr. Moderate
    """
    name = "Mr. Moderate"

    def strategy(self, opponent):
        """ This example is the Cooperator strategy: always cooperate. """
        return Action.C
