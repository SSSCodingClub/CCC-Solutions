drops = int(input())
left, right, top, bottom = 100, 0, 0, 100

for i in range(drops):
    point = input().split(",")
    x, y = int(point[0]), int(point[1])

    left = min(left, x)
    right = max(right, x)
    bottom = min(bottom, y)
    top = max(top, y)

print(f"{left - 1}, {bottom - 1}")
print(f"{right + 1}, {top + 1}")
