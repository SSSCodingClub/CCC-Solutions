from string import digits

instructions = input()

split = False
output = ""

for char in instructions:
    if char == "+":
        output += " tighten "
    elif char == "-":
        output += " loosen "
    elif char in digits:
        output += char
        split = True
    elif split:
        output += "\n" + char
        split = False
    else:
        output += char

print(output)
