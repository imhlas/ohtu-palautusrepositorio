import unittest
from statistics_service import StatisticsService, sort_by_points
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_returns_player(self):
        player = self.stats.search("Semenko")

        expected_player = Player("Semenko", "EDM", 4, 12)
        self.assertEqual(player.name, expected_player.name)

    def test_search_with_wrong_player(self):
        player = self.stats.search("Testi")

        self.assertEqual(player, None)

    def test_players_in_team(self):
        players = self.stats.team("EDM")

        self.assertEqual(len(players), 3)

    def test_sort_by_points(self):
        player = Player("TestPlayer", "TMP", 10, 20)
        self.assertEqual(sort_by_points(player), 30) 

    def test_top_players(self):
        top_players = self.stats.top(2)

        self.assertEqual(len(top_players), 3)
