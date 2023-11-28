class TennisGame:
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
        score = ""
        temp_score = 0

        if self.player1_score == self.player2_score:
            score = self.score_tie()

        elif self.player1_score >= 4 or self.player2_score >= 4:
            score = self.score_advantage_or_win()

        else:
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.player1_score
                else:
                    score = score + "-"
                    temp_score = self.player2_score

                if temp_score == 0:
                    score = score + "Love"
                elif temp_score == 1:
                    score = score + "Fifteen"
                elif temp_score == 2:
                    score = score + "Thirty"
                elif temp_score == 3:
                    score = score + "Forty"

        return score

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
