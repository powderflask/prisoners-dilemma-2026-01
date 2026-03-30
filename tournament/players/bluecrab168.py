# Auto-generated from GitHub Issue submission
# Author: bluecrab168
# Generated: 2026-03-30T19:07:57.979354+00:00Z

# Imports for building your Player
from axelrod import Player, Action

class Defector(Player):
    """List the names of all students who worked on this class here. """
    name = "Ms. Mean"

    def strategy(self, opponent):
        """ This example is the Cooperator strategy: always defect. """
        return Action.D
