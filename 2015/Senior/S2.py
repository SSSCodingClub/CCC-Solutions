j, a = int(input()), int(input())

jerseys = []

sizes = {"L": 3, "M": 2, "S": 1}
for _ in range(j):
    size = input()
    # if size == "L":
    #     jerseys.append(3)
    
    jerseys.append(sizes[size]) # Convert jersey size to int for easy comparison

requests = 0
for _ in range(a):
    size, number = input().split()
    size = sizes[size]

    if jerseys[int(number) - 1] >= size:
        requests += 1
        jerseys[int(number) - 1] = 0

print(requests)
