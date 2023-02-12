rows, cols, changes = int(input()), int(input()), int(input())

canvas = [[False for _ in range(cols)] for _ in range(rows)]

# Way to much work to type out!
# canvas = []
# for _ in range(rows):
#     canvas.append([])
#     for _ in range(cols):
#         canvas[-1].append(False) # add False to latest list

# '_' means that we aren't going to use it in for loop. write good python
row_changes = [False for _ in range(rows)]
col_changes = [False for _ in range(cols)]

for _ in range(changes):
    position, index = input().split()
    index = int(index) - 1

    if position == "R": # True -> not True = False
        row_changes[index] = not row_changes[index]
    else:
        col_changes[index] = not row_changes[index]

for i in range(rows):
    if row_changes[i]:
        for j in range(cols):
            canvas[i][j] = not canvas[i][j]

for i in range(cols):
    if col_changes[i]:
        for j in range(rows):
            canvas[j][i] = not canvas[j][i]

total = 0
for i in range(rows):
    for j in range(cols):
        if canvas[i][j]:
            total += 1

print(total)