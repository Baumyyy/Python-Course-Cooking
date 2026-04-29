class CalmnessEngine:
    def __init__(self, calmness=100):
        self.calmness = calmness

    def apply(self, mood):
        if mood == 'rage':
            change = -35
        elif mood == 'calm':
            change = 10
        else:
            change = -5

        self.calmness = max(0, min(self.calmness + change, 120))
        return change

    def is_game_over(self):
        return self.calmness == 0
