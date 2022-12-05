class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1_score = 0
        self.p2_score = 0
        self.score_names = {
            0:"Love",
            1:"Fifteen",
            2:"Thirty",
            3:"Forty"
        }
        self.winscore = 4

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.p1_score += 1
        else:
            self.p2_score += 1

    def get_score(self):
        if self.p1_score == self.p2_score:
            return self.get_tie()
        elif (self.p1_score >= self.winscore 
                or self.p2_score >= self.winscore):
           return self.get_win()
        else:
            return self.get_uneven_score()            
        
    def get_tie(self):
        if self.p1_score >= self.winscore:
            return "Deuce"
        else:
            return f"{self.score_names[self.p1_score]}-All"
        
    def get_win(self):
        result_difference = self.p1_score - self.p2_score
        if result_difference > 0:
            leader = self.player1_name
        else:
            leader = self.player2_name
        if abs(result_difference) == 1:
            return f"Advantage {leader}"
        return f"Win for {leader}"
    
    def get_uneven_score(self):
        score = f"{self.score_names[self.p1_score]}-"
        score += f"{self.score_names[self.p2_score]}"
        return score
        temp_score = 0
        for i in range(1, 3):
            if i == 1:
                temp_score = self.p1_score
            else:
                score = score + "-"
                temp_score = self.p2_score

            if temp_score == 0:
                score = score + "Love"
            elif temp_score == 1:
                score = score + "Fifteen"
            elif temp_score == 2:
                score = score + "Thirty"
            elif temp_score == 3:
                score = score + "Forty"
        return score

