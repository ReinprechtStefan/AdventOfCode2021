with open('input.txt') as f:
    lines = f.readlines()

    depth_increased = 0

    for i in range(len(lines)):
        if (i == 0):
            # don't check first sonar input
            continue

        if (int(lines[i]) > int(lines[i-1])):
            depth_increased = depth_increased + 1

    print(depth_increased) # 1559
