G = int(input())
P = int(input())
gates = [False for _ in range(G)]

closed = False
can_land = False
counter = 0

for _ in range(P):
    g = int(input())

    if not closed:
        can_land = False
        for d in range(g, 0, -1): # range(5) 0, 1, 2, 3, 4 ||| range(5, 0, -1) 5, 4, 3, 2, 1
            if gates[d-1] == False:
                gates[d-1] = True
                can_land = True
                break
        if can_land:
            counter += 1
        else:
            closed = True

print(counter)
