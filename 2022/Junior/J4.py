X = int(input())
same = []
for i in range(X):
    same.append(input().split())

Y = int(input())
different = []
for i in range(Y):
    different.append(input().split())

G = int(input())
names = dict()
for i in range(G):
    group = input().split()
    for n in group:
        names[n] = i

violated = 0

for name1, name2 in same:
    if names[name1] != names[name2]:
        violated += 1
for name1, name2 in different:
    if names[name1] == names[name2]:
        violated += 1

print(violated)
