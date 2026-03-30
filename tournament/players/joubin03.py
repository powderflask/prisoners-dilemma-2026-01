# Auto-generated from GitHub Issue submission
# Author: joubin03
# Generated: 2026-03-30T19:20:47.928333+00:00Z

from axelrod import Player, Action

class JoubinPlayer(Player):
    """
    Name: Joubin Eghbali
    Strategy: Tit for Tat (copy opponent's last move)
    """

    name = "Joubin Player"

    def strategy(self, opponent: Player) -> Action:
        if not opponent.history:
            return Action.C
        return opponent.history[-1]
