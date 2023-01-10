instructions = [] 

while True:
    current = input()
    if current == "99999":
        break
    instructions.append(current)

previous = None
for instruction in instructions: #57234
    total = int(instruction[0]) + int(instruction[1])
    steps = int(instruction[2] + instruction[3] + instruction[4]) # "And" + "rew" = "Andrew" for strings
    if total == 0:
        print(previous, steps)
    elif total % 2 == 0: # Even
        print("right", steps)
        previous = "right"
    else:
        print("left", steps)
        previous = "left"