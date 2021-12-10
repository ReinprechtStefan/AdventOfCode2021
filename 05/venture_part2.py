import numpy as np


class VentDirection:
    positions = []

    def __init__(self, source_val, target_val):
        self.positions = []
        source_position = (int(source_val[0]), int(source_val[1]))
        target_position = (int(target_val[0]), int(target_val[1]))

        self.positions.append(self.calc_positions(
            source_position, target_position))

    def calc_positions(self, source_pos, target_pos):

        if source_pos[0] != target_pos[0] and source_pos[1] != target_pos[1]:
            #x_values = []
            # if source_pos[0] < target_pos[0]:
            #    x_values = range(source_pos[0] + 1, target_pos[0] - 1)
            # else:
            #    x_values = range(target_pos[0] + 1, source_pos[0] - 1)

            #y_values = []
            # if source_pos[1] < target_pos[1]:
            #    y_values = range(source_pos[1] + 1, target_pos[1] - 1)
            # else:
            #    y_values = range(target_pos[1] + 1, source_pos[1] - 1)

            # for i in range(len(x_values)):
            #    self.positions.append((x_values[i], y_values[i]))
            steigung = round(
                (target_pos[1] - source_pos[1]) / (target_pos[0] - source_pos[0]))
            unterschied = target_pos[1] - steigung * target_pos[0]
            coords = ([(x, round(steigung * x + unterschied))
                       for x in (range(source_pos[0], target_pos[0] + 1) if source_pos[0] < target_pos[0] else range(target_pos[0], source_pos[0] + 1))])
            for coord in coords:
                self.positions.append(coord)
        else:
            self.positions.append(source_pos)
            self.positions.append(target_pos)

            if source_pos[0] != target_pos[0]:
                if source_pos[0] < target_pos[0]:
                    for i in range(source_pos[0] + 1, target_pos[0]):
                        self.positions.append((i, source_pos[1]))
                else:
                    for i in range(target_pos[0] + 1, source_pos[0]):
                        self.positions.append((i, source_pos[1]))
            else:
                if source_pos[1] < target_pos[1]:
                    for i in range(source_pos[1] + 1, target_pos[1]):
                        self.positions.append((source_pos[0], i))
                else:
                    for i in range(target_pos[1] + 1, source_pos[1]):
                        self.positions.append((source_pos[0], i))

    def get_positions(self):
        return self.positions


with open('input.txt') as f:
    lines = f.readlines()

    directions = []

    for line in lines:
        vent_parts = line.split(" -> ")
        directions.append(VentDirection(
            vent_parts[0].split(","), vent_parts[1].split(",")))

    positions = {}

    for direction in directions:
        for pos in direction.get_positions():
            if pos == None:
                continue

            # print(pos)
            if positions.get(pos) == None:
                # print("Insert new position: ", pos)
                positions[pos] = 1
            else:
                # print("Update position: ", pos)
                positions[pos] = int(positions.get(pos)) + 1

    result = 0
    for i in positions.values():
        if int(i) > 1:
            result += 1

    print(result)
