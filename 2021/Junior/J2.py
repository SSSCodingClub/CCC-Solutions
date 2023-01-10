N = int(input())

bids = [] # [("Andrew", 100), ("Saahil", 100)]

for i in range(N):
    name = input()
    bid = int(input())
    bids.append((name, bid))

highest_bid = bids[0]
for i in bids:
    name, bid = i
    if highest_bid[1] < bid:
        highest_bid = i

print(highest_bid[0])
