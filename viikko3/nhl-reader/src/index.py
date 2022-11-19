from player import Player
import requests

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_by_nationality("FIN")

    for player in players:
        print(player)

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def read(self):
        return requests.get(self.url).json()
        
class PlayerStats:
    def __init__(self, reader):
        self.reader = reader.read()
    
    def top_by_nationality(self, nationality):
        players = []
        def in_nation(x):
            return x['nationality'] == nationality

        nationread = filter(in_nation, self.reader)

        for player_dict in nationread:

            player = Player(
            player_dict['name'],
            player_dict['goals'],
            player_dict['assists']
            )
            players.append(player)

        players = sorted(players, key=lambda x: x.goals+x.assists, reverse=True)
        return players



if __name__ == "__main__":
    main()
