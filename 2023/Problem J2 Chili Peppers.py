N = int(input())
T = 0
for i in range(N):
    pepper = input()
    if pepper == "Poblano":
        T += 1500
    elif pepper == "Mirasol":
        T += 6000
    elif pepper == "Serrano":
        T += 15500
    elif pepper == "Cayenne":
        T += 40000
    elif pepper == "Thai":
        T += 75000
    elif pepper == "Habanero":
        T += 125000

print(T)