G = int(input())
P = int(input())
docks = [False for _ in range(G)]

closed = False
can_land = False
counter = 0

for _ in range(P):
	g = int(input())
	if not closed:
		can_land = False
		for d in range(g, 0, -1):
			if docks[d-1] == False:
				docks[d-1] = True
				can_land = True
				break
		if not can_land:
			closed = True
		else:
			counter += 1
print(counter)
