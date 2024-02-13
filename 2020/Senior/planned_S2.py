from queue import Queue


def factors(n):
    factors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if i > M or n // i > N:
                continue
            factors.append(i)
            factors.append(n // i)
    return factors

M = int(input())
N = int(input())

grid = tuple(tuple(map(int, input().split())) for _ in range(M))
target = (M - 1, N - 1)
start = (0, 0)
q = Queue()
q.put(start)

seen = set()
while not q.empty():
    r, c = q.get()
    if (r, c) == target:
        print("yes")
        quit()
    else:
        n = grid[r][c]
        if n in seen:
            continue
        seen.add(n)
        f = factors(n)
        for factor in f:
            if factor <= M and n // factor <= N:
                q.put((factor - 1, n // factor - 1))
print("no")
