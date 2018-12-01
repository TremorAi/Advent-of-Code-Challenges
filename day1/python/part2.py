import random
thing = open("day1/input.txt", "r")
numthing = 0
listthing = set()
thang = True
lines = list(thing)
count = 0
while thang:
    count = count + 1
    for line in lines:
        op = line[0]
        num = line[1:]
        if op == "-":
            numthing -= int(num)
        elif op == "+":
            numthing += int(num)
        if numthing not in listthing:
            listthing.add(numthing)
        else:
            thang = False
            break
print(f"It took: {count} loops to get the correct answer")
print(numthing)
