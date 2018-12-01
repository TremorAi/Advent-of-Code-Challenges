thing = open("day1/input.txt", "r")
numthing = 0
for line in thing:
    op = line[0]
    num = line[1:]
    if op == "-":
        numthing -= int(num)
    elif op == "+":
        numthing += int(num)
print(numthing)
