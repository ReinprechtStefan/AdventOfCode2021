import numpy as np

def calc_fuel(diff):
    fuel = 0
    for i in range(diff + 1):
        fuel += i
    return fuel

with open('input.txt') as f:
    lines = f.readlines()

    craps = list(map(int, lines[0].split(",")))

    #print(len(craps))
    #avg = int(np.round(np.average(craps)))

    min = np.min(craps)
    max = np.max(craps) + 1

    print(min, max)

    pos = 0
    
    fuel_for_pos = -1
    for i in range(min, max):
        fuel = 0
        for crap in craps:
            if crap < i:
                fuel += calc_fuel(i - crap)
            elif crap > i:
                fuel += calc_fuel(crap - i)

        if fuel_for_pos == -1:
            fuel_for_pos = fuel
            pos = i

        if fuel_for_pos != -1 and fuel <= fuel_for_pos:
            fuel_for_pos = fuel
            pos = i

        print(i, fuel)

    print(fuel_for_pos)

        