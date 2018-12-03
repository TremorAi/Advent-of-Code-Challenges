import numpy as np
file_input = list(map(str.strip, open("day3/input.txt").readlines()))

# y than x
grid_array = np.zeros((1000, 1000))

for line in file_input:
    line_split = line.split(" ")
    # print(
    #     f"id: {line_split[0]} location from edge: {line_split[2]} width/height: {line_split[3]}")
    width_height = line_split[3].split("x")
    padding = line_split[2].split(",")
    top = int(padding[1].replace(":", ""))
    left = int(padding[0])
    width = int(width_height[0])
    height = int(width_height[1])
    # print(f"left: {left} top: {top}")
    for w in range(width):
        for h in range(height):
            grid_array[top + h, left + w] += 1

sum_area = grid_array >= 2
print(sum_area.sum())
