#p = 5b - 400

b = int(input())
p = (5 * b) - 400
print(p)

if p == 100:
    #Equal to sea level
    print(0)
elif p < 100:
    #Above sea level
    print(1)
else:
    #Below sea level
    print(-1)