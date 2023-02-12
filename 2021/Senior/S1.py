n = int(input())

l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

ans = 0
for i in range(n):
    ans += (l1[i] + l1[i+1]) * l2[i] / 2 # Formula for trapezoid area = (b1 + b2) * h / 2

print(ans)
# print(int(ans)) # turns it into a whole number by ignoring all decimals after