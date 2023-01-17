drops = int(input())
left, right, top, bottom = 100, 0, 0, 100

for i in range(drops):
    x, y = tuple(map(int, input().split(",")))

    left = min(left, x)
    right = max(right, x)
    bottom = min(bottom, y)
    top = max(top, y)

print(left - 1, bottom - 1, sep=",")
print(right + 1, top + 1, sep=",")
