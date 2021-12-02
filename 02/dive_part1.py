with open('input.txt') as f:
    lines = f.readlines()

    depth = 0
    vertical = 0

    for line in lines:
        operation = line.split(" ")[0]
        value = int(line.split(" ")[1])

        if (operation == 'forward'):
            vertical += value
        elif (operation == 'down'):
            depth += value
        elif (operation == 'up'):
            depth -= value
        else:
            print('uff')
    
    print("depth:", depth)
    print("vertical:", vertical)
    print("result:", (depth * vertical))