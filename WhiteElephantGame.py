import random
class WhiteElephantGame:
    def __init__(self, players):
        self.players = players
        self.game = {x: None for x in range(players)}
        self.gifts = [x for x in range(players)]

    def completed(self):
        return all(x is not None for x in self.game.values())

    def no_gifts_selected(self):
        return all(x is None for x in self.game.values())
    
    def random_number(self):
        return random.randint(0, self.players - 1)

    def open_gift(self, person, gift):
        self.game[person] = gift
    
    def steal_gift(self, person, thief):
        # thief takes person's gift
        # thief
        if self.game[thief] is not None:
            return
        self.game[thief] = self.game[person]
        self.game[person] = None
    
    def nextMove(self):
        if self.no_gifts_selected():
            # pick first give 
        # steal

        # assign random 
