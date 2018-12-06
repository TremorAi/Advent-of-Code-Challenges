import numpy as np
import re
file_input = list(map(str.strip, open("day6/input.txt").readlines()))
grid_array = np.zeros((500, 500))
for line in file_input:
    new_line = line.split(",")
    print(new_line[1])
    grid_array[int(new_line[0]), int(new_line[1])] += 1
print(grid_array)

# |x1 - y1| + |x2 - y2|
# np.savetxt('file.out', grid_array, delimiter=',')
