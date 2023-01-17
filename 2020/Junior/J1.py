small = int(input())
medium = int(input())
large = int(input())

happiness = 1 * small + 2 * medium + 3 * large

if happiness >= 10:
    print("happy")
else:
    print("sad")