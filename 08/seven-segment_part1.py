with open('input.txt') as f:
    lines = f.readlines()

    counter = 0

    for line in lines:
        right_part = line.split(" | ")[1]

        for segment in right_part.strip().split(" "):
            #print(segment, len(segment))
            if len(segment) in [2,3,4,7]:
                counter += 1
            #else:
                #print("NO ", segment, len(segment))


    print(counter)
