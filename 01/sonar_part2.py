with open('input.txt') as f:
    lines = [int(i) for i in f.readlines()]

    depth_increased = 0

    for i in range(0, len(lines) - 3):
        
        last_sum = sum(lines[i-1:i+2])
        current_sum = sum(lines[i:i+3])
        
        if (current_sum > last_sum):
            depth_increased = depth_increased + 1

    print(depth_increased) # 1600
