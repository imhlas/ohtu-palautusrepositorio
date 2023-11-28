class TennisGame:
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]
    ONE_POINT = 1

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self.score_tie()

        elif self.player1_score >= 4 or self.player2_score >= 4:
            return self.score_advantage_or_win()

        else:
            return f"{self.SCORE_NAMES[self.player1_score]}-{self.SCORE_NAMES[self.player2_score]}"

    def score_tie(self):
        scores = ["Love-All", "Fifteen-All", "Thirty-All"]
        return scores[self.player1_score] if self.player1_score < 3 else "Deuce"

    def score_advantage_or_win(self):
        difference = self.player1_score - self.player2_score

        if difference == self.ONE_POINT:
            return "Advantage player1"
        elif difference == -self.ONE_POINT:
            return "Advantage player2"
        elif difference >= self.ONE_POINT +1:
            return "Win for player1"
        else:
            return "Win for player2"

