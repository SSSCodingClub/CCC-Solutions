N = int(input())

bids = []

for i in range(N):
    bids.append((input(), int(input())))

highest_bid = None
for name, bid in bids:
    if highest_bid is None or highest_bid[1] < bid:
        highest_bid = (name, bid)

print(highest_bid[0])
