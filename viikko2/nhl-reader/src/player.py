class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.team = dict['team']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.total = self.goals + self.assists

    def __str__(self):
        return f"{self.name:<20} {self.team:<3} {self.goals:>2} + {self.assists:>2} = {self.total:<3}"
