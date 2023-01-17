#j3 solution!
drops = int(input())  # N

left = 100
right = 0
top =  0
bottom = 100

for i in range(drops): # 1,2 -> "1,2" -> ["1", "2"] -> [int("1"), int("2")] -> [1, 2] -> x = 1 y = 2
    X, Y = list(map(int,input().split(",")))

    left = min(left, X)
    right = max(right, X)
    bottom = min(bottom, Y)
    top = max(top, Y)

print(left-1, bottom - 1, sep=",")
print(right+1, top + 1, sep=",")
