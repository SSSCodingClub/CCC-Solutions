N = int(input())

h = tuple(map(int, input().split()))
w = tuple(map(int, input().split()))

area = 0
for i in range(N):
    area += (h[i] + h[i+1]) * w[i] / 2

print(area)
