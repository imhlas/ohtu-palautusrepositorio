class PlayerStats:
    def __init__(self, player_reader):
        self.player_reader = player_reader

    def top_scorers_by_nationality(self, nationality):
        players = self.player_reader.get_players()

        players_by_nationality = []

        for player in players:
            if player.nationality == nationality:
                players_by_nationality.append(player)

        players_by_nationality.sort(key=lambda x: x.total, reverse=True)

        return players_by_nationality
