# Auto-generated from GitHub Issue submission
# Author: powderflask
# Generated: 2026-01-06T04:13:01.470575+00:00Z

from axelrod import Player, Action


class Cooperator(Player):
    name = "Mr. Nice Guy"

    def strategy(self, opponent):
        """Disregard whatever happened before, always be nice and cooperate."""
        return Action.C
