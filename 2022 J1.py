R = int(input()) # regular boxes
S = int(input()) # small boxes

total = R * 8 + S * 3
left_over = total - 28 # one cupcake per student

print(left_over)
