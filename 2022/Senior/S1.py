N = int(input())

# find # 5's and # 4's

answer = 0
for five in range(0, N + 1, 5):
    if (N- five) % 4 == 0:
        answer += 1

print(answer)