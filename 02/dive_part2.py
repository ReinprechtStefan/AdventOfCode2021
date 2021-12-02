with open('input.txt') as f:
    lines = f.readlines()

    depth = 0
    vertical = 0
    aim = 0

    for line in lines:
        operation = line.split(" ")[0]
        value = int(line.split(" ")[1])

        if (operation == 'forward'):
            vertical += value
            depth += value * aim
        elif (operation == 'down'):
            aim += value
        elif (operation == 'up'):
            aim -= value
        else:
            print('uff')
    
    print("depth:", depth)
    print("vertical:", vertical)
    print("result:", (depth * vertical))