import re
file_input = (open('input.txt').read())
last_char = len(file_input)
orginal = file_input

for x in "abcdefghijklmnopqrstuvwxyz":
    test = True
    file_input = orginal.replace(x, "").replace(x.upper(), "")
    while test:
        before = len(file_input)
        for i in "abcdefghijklmnopqrstuvwxyz":
            file_input = file_input.replace(i + i.upper(), "")
            file_input = file_input.replace(i.upper() + i, "")
        if len(file_input) == before:
            test = False
    if len(file_input) < last_char:
        last_char = len(file_input)
print(last_char)
