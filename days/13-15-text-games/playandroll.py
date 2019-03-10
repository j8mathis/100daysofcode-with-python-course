class Roll:
    def __init__(self, name, defeat):
        self.name = name
        self.defeat = defeat

    def can_defeat(self, p_roll):

        if p_roll == self.defeat:
            return True
        else:
            return False


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_score(self):
        self.score += 1
