import random
thing = open("day1/input.txt", "r")
numthing = 0
listthing = set()
thang = True
lines = list(thing)
while thang:
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

# print(listthing)
print(numthing)
