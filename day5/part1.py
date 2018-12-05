import re
file_input = (open('day5/input.txt').read())
last_char = ""
test = True

while test:
    last_char = file_input
    for i in "abcdefghijklmnopqrstuvwxyz":
        file_input = file_input.replace(i + i.upper(), "")
        file_input = file_input.replace(i.upper() + i, "")
        print(len(file_input))
    if file_input == last_char:
        test = False
print(len(file_input))
