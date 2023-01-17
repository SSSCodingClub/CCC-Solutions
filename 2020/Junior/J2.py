#j2 solution

p = int(input())
n = int(input())
r = int(input())

tot = n
day = 0

while tot <= p:
    day += 1
    n *= r
    tot += n

print(day)