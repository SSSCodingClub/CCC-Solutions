total = 0


def dfs(node, depth, has_branched, direction, just_started=False):
    y, x = node
    if depth >= len(word):
        return
    if word[depth] != grid[y][x]:
        return

    if not (0 <= x < C and 0 <= y < R):
        return

    # check if we found the word
    if depth == len(word) - 1:
        global total
        total += 1
        return
    if direction == 0:  # UP
        if y - 1 >= 0 and grid[y - 1][x] == word[depth + 1]:
            dfs((y - 1, x), depth + 1, has_branched, direction)
        if not has_branched and not just_started:
            dfs((y, x), depth, not has_branched, (direction - 2) % 8)
            dfs((y, x), depth, not has_branched, (direction + 2) % 8)
    elif direction == 1:  # TR
        if y - 1 >= 0 and x + 1 < C and grid[y - 1][x + 1] == word[depth + 1]:
            dfs((y - 1, x + 1), depth + 1, has_branched, direction)
        if not has_branched and not just_started:
            dfs((y, x), depth, not has_branched, (direction - 2) % 8)
            dfs((y, x), depth, not has_branched, (direction + 2) % 8)
    elif direction == 2:  # R
        if x + 1 < C and grid[y][x + 1] == word[depth + 1]:
            dfs((y, x + 1), depth + 1, has_branched, direction)
        if not has_branched and not just_started:
            dfs((y, x), depth, not has_branched, (direction - 2) % 8)
            dfs((y, x), depth, not has_branched, (direction + 2) % 8)
    elif direction == 3:  # BR
        if y + 1 < R and x + 1 < C and grid[y + 1][x + 1] == word[depth + 1]:
            dfs((y + 1, x + 1), depth + 1, has_branched, direction)
        if not has_branched and not just_started:
            dfs((y, x), depth, not has_branched, (direction - 2) % 8)
            dfs((y, x), depth, not has_branched, (direction + 2) % 8)
    elif direction == 4:  # B
        if y + 1 < R and grid[y + 1][x] == word[depth + 1]:
            dfs((y + 1, x), depth + 1, has_branched, direction)
        if not has_branched and not just_started:
            dfs((y, x), depth, not has_branched, (direction - 2) % 8)
            dfs((y, x), depth, not has_branched, (direction + 2) % 8)
    elif direction == 5:  # BL
        if y + 1 < R and x - 1 >= 0 and grid[y + 1][x - 1] == word[depth + 1]:
            dfs((y + 1, x - 1), depth + 1, has_branched, direction)
        if not has_branched and not just_started:
            dfs((y, x), depth, not has_branched, (direction - 2) % 8)
            dfs((y, x), depth, not has_branched, (direction + 2) % 8)
    elif direction == 6:  # L
        if x - 1 >= 0 and grid[y][x - 1] == word[depth + 1]:
            dfs((y, x - 1), depth + 1, has_branched, direction)
        if not has_branched and not just_started:
            dfs((y, x), depth, not has_branched, (direction - 2) % 8)
            dfs((y, x), depth, not has_branched, (direction + 2) % 8)
    elif direction == 7:  # TL
        if y - 1 >= 0 and x - 1 >= 0 and grid[y - 1][x - 1] == word[depth + 1]:
            dfs((y - 1, x - 1), depth + 1, has_branched, direction)
        if not has_branched and not just_started:
            dfs((y, x), depth, not has_branched, (direction - 2) % 8)
            dfs((y, x), depth, not has_branched, (direction + 2) % 8)


word = input()
R = int(input())
C = int(input())

grid = []
for i in range(R):
    grid.append(list(input().split()))  #

total = 0
for r in range(R):
    for c in range(C):
        if grid[r][c] == word[0]:
            for i in range(8):
                dfs((r, c), 0, False, i, True)

print(total)
