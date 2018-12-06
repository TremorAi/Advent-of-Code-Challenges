import numpy as np
file_input = list(map(str.strip, open("input.txt").readlines()))

storage = 0
centers = []
number_thing = 10000
counter = 0
storage_dict = {}
infinite_ids = set()


def manhattan_distance(point_1_x, point_1_y, point_2_x, point_2_y):
    thing = abs(point_1_x - point_2_x) + abs(point_1_y - point_2_y)
    return thing


grid_array = np.zeros((348, 359))
for line in file_input:
    new_line = line.split(",")
    grid_array[int(new_line[0]), int(new_line[1])] += 1
    centers.append((int(new_line[0]), int(new_line[1])))

for index, p in np.ndenumerate(grid_array):
    for i, point in enumerate(centers):
        test = manhattan_distance(point[0], point[1], index[0], index[1])
        storage += test
    if storage <= 10000:
        grid_array[index] = 1
        counter += 1
    storage = 0

    number_thing = 1000000
for index, p in np.ndenumerate(grid_array):
    if index[0] >= 347:
        infinite_ids.add(p)
    elif index[0] <= 0:
        infinite_ids.add(p)
    if index[1] >= 358:
        infinite_ids.add(p)
    if index[1] <= 0:
        infinite_ids.add(p)
for index, p in np.ndenumerate(grid_array):
    if p not in infinite_ids and p != 0:
        if p not in storage_dict.keys():
            storage_dict[p] = 1
        else:
            storage_dict[int(p)] += 1

print(counter)
