players = int(input())
gold = 0

for i in range(players):
    goals, fouls = int(input()), int(input())
    stars = (goals * 5) - (fouls * 3)
    if stars > 40:
        gold += 1

print(gold, end="")
if gold == players:
    print("+")
