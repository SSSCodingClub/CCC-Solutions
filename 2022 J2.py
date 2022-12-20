players = int(input()) # number of players
gold = 0 # number of gold players

for i in range(players):
    goals = int(input())
    fouls = int(input())
    stars = goals * 5 - fouls * 3
    if stars > 40:
        gold += 1

print(gold, end="") # end is an optional argument that is by default '\n' newline character
# if number of gold players is the same as number of players, this means everyone is a gold player
if gold == players:
    print("+")