N = int(input())

output = 0
for five in range(0, N + 1, 5):
    if (N - five) % 4 == 0:
        output += 1

print(output)
