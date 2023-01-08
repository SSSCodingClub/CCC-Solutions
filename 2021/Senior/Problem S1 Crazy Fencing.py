ans = 0
n = int(input())

l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

for i in range(n):
    ans += (l1[i] + l1[i + 1]) * l2[i] / 2

print(ans)
