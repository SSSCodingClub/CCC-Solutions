def flip_horizontal(grid):
	return [[grid[1][0], grid[1][1]], [grid[0][0], grid[0][1]]]


def flip_vertical(grid):
	return [[grid[0][1], grid[0][0]], [grid[1][1], grid[1][0]]]


commands = input()
grid = [[1, 2], [3, 4]]

h = commands.count('H')
v = commands.count('V')

# Same as:
# h = 0
# v = 0
# for c in commands:
# 	if c == 'H':
# 		h += 1
# 	elif c == 'V':
# 		v += 1


if h % 2 == 1:
	grid = flip_horizontal(grid)

if v % 2 == 1:
	grid = flip_vertical(grid)

# Brute Force:
# for c in commands:
# 	if c == 'H':
# 		grid = flip_horizontal(grid)
# 	elif c == 'V':
# 		grid = flip_vertical(grid)


for i in grid:
	for j in i:
		print(j, end=' ')
	print()
