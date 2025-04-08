class Player:
    def __init__(self, name, position, rating):
        self.name = name
        self.position = position
        self.rating = rating

class Team:
    def __init__(self):
        self.players = []

    def draft_player(self, player):
        self.players.append(player)

# Sample player data
player1 = Player("Lionel Messi", "Forward", 93)
player2 = Player("Cristiano Ronaldo", "Forward", 92)

# Team draft
my_team = Team()
my_team.draft_player(player1)
my_team.draft_player(player2)

for player in my_team.players:
    print(f"{player.name} - {player.position} - Rating: {player.rating}")