N = int(input())

gold_team = True
number_star_players = 0

for player in range(N):
    points = int(input()) * 5
    fouls = int(input()) * 3
    star_rating = points - fouls
    if star_rating > 40:
        number_star_players += 1
    else:
        gold_team = False

print(number_star_players, end="")
if gold_team:
    print('+')
