people, infected, daily = int(input()), int(input()), int(input())
days = 0
while infected < people:
    infected += daily * infected
    days += 1

print(days)
