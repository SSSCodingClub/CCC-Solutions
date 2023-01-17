from string import digits # digits = "1234567890"

instructions = input() # string input

output = ""
split = False # go to new line when this is true

for char in instructions: # char is short for character
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
    else: # is a letter.
        output += char

print(output)
# AFB+8HC-4