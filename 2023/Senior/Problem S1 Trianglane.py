C = int(input())
top_row = tuple(map(int, input().split()))
bot_row = tuple(map(int, input().split()))

output = 0
for tile in top_row:
    if tile == 1:
        output += 3
for tile in bot_row:
    if tile == 1:
        output += 3

for i in range(C-1):
    if top_row[i] == 1 and top_row[i + 1] == 1:
        output -= 2
    if bot_row[i] == 1 and bot_row[i + 1] == 1:
        output -= 2
    if i % 2 == 0 and top_row[i] == 1 and bot_row[i] == 1:
        output -= 2
if (C-1) % 2 == 0 and top_row[-1] == 1 and bot_row[-1] == 1:
    output -= 2

print(output)
