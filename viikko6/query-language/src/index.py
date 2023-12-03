from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or
from querybuilder import QueryBuilder

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()
    matcher = query.build()

    pelaajien_maara = 0
    for player in stats.matches(matcher):
        print(player)
        pelaajien_maara += 1

    print("Pelaajien määrä:", pelaajien_maara)

if __name__ == "__main__":
    main()
