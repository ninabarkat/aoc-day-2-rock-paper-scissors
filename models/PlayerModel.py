class PlayerModel:
    score: int
    choice: str

    def __init__(self):
        self.score = 0

    def increase_score(self, n):
        self.score += n

    def get_score(self):
        return self.score
