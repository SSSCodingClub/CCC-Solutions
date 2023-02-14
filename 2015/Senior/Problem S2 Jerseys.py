j, a = int(input()), int(input())
sizes = {"L": 3, "M": 2, "S": 1}
jerseys = []

for _ in range(j):
    size = input()
    jerseys.append(sizes[size])
requests = 0

for _ in range(a):
    size, number = input().split()
    size = sizes[size]

    if jerseys[int(number) - 1] >= size:
        requests += 1
        jerseys[int(number) - 1] = 0

print(requests)
