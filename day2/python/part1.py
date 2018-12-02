thing = open("day2/input.txt", "r")
num2 = 0
num3 = 0

for line in thing:
    double_list = []
    triple_list = []
    testbool1 = True
    testbool2 = True
    for i in line:
        if line.count(i) == 2 and testbool1:
            if i not in double_list:
                testbool1 = False
                double_list.append(i)
                num2 += 1

        elif line.count(i) == 3 and testbool2:
            if i not in triple_list:
                testbool2 = False
                triple_list.append(i)
                num3 += 1


print(num2 * num3)
