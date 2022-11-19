class Player:
    def __init__(self, name, goals, assists):
        self.name = name
        self.goals = goals
        self.assists = assists

    
    def __str__(self):
        return f"{self.name:20} {self.goals} + {self.assists} = {self.goals + self.assists}"
