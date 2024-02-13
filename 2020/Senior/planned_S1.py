N = int(input())

positions = []

for i in range(N):
    T,X = tuple(map(int, input().split()))
    positions.append((T,X))

positions.sort()

output = None
for i in range(1,N):
    speed = abs(positions[i][1]-positions[i-1][1])/abs(positions[i][0]-positions[i-1][0])
    if output is None or speed > output:
        output = speed

print(output)