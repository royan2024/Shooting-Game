class ScoreCalculator:
    def __init__(self):
        self.hit = 0
        self.kill = 0

    def calculate(self, elapsed_time, is_win):
        if is_win:
            return self.hit * 1000 + self.kill * 10000 + max(0, 60 - elapsed_time) * 1000
        else:
            return self.hit * 1000 + self.kill * 10000