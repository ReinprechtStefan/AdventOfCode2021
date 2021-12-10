def chunks(l, n):
    n = max(1, n)
    return (l[i:i+n] for i in range(0, len(l), n))

with open('example-input.txt') as f:
    lines = f.readlines()

    fish_population = list(map(int, lines[0].split(",")))

    for day in range(256):
        print(day)
        new_fishes = 0
        for i, fish in enumerate(fish_population):
            if fish == 0:
                new_fishes += 1
                fish_population[i] = 6
            else:
                fish_population[i] = fish - 1
    
        for _ in range(new_fishes):
            fish_population.append(8)
    
    print(len(fish_population))
            

