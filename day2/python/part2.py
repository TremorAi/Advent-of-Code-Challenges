file_input = list(map(str.strip, open("day2/input.txt").readlines()))


container = []


def char_difference(string1, string2):
    counter = 0
    for i in range(len(string1)):
        if string1[i] == string2[i]:
            # print(f"{string1} {string2}")
            pass
        else:
            counter += 1
        if counter > 1:
            break

    return counter


for line in file_input:
    for line2 in file_input:
        test1 = char_difference(line, line2)

        if test1 == 1:
            newline = ""
            for i in range(len(line)):
                if line[i] == line2[i]:
                    newline += line[i]
            print(f"{newline}")
            break
