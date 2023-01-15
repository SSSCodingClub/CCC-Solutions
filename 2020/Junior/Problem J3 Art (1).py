drops = int(input())
coordinates = []
for i in range(drops):
    x, y = input().split(",")
    coordinates.append((int(x), int(y)))

left, right, top, bottom = None, None, None, None
for point in coordinates:
    if left is None or point[0] < left:
        left = point[0]
    if right is None or point[0] > left:
        right = point[0]
    if top is None or point[1] > top:
        top = point[1]
    if bottom is None or point[1] < bottom:
        bottom = point[1]

print(f"{left - 1}, {bottom - 1}")
print(f"{right + 1}, {top + 1}")
