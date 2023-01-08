instructions = input()

sequence = ""
was_number = False
for i in instructions:
    if i in "1234567890":
        sequence += i
        was_number = True
    elif i == "+":
        sequence += " tighten "
    elif i == "-":
        sequence += " loosen "
    else: # is a letter
        if was_number:
            print(sequence)
            sequence = ""
            was_number = False
        sequence += i
print(sequence)
