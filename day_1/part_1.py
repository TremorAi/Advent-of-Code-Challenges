total_number = 0

with open('data.txt', 'r') as file:
    content = file.readlines()
    for line in content:
        operator = line[:1]
        number = int(line.strip(operator))

        if operator == '-':
            total_number -= number
        elif operator == '+':
            total_number += number

    print(total_number)
