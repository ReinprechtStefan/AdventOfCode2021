with open('input.txt') as f:

    sum = 0

    for line in f.readlines():
        input_data, output = line.split('|')
        #print(input_data, output)

        input_data_map = {}
        for string in input_data.split():
            input_data_map[len(string)] = set(string)

        #print(input_data_map)

        translated_number = ''
        for o in map(set, output.split()):
            #print(o)

            if len(o) == 2:
                translated_number += '1'
            elif len(o) == 3:
                translated_number += '7'
            elif len(o) == 4:
                translated_number += '4'
            elif len(o) == 7:
                translated_number += '8'
            elif len(o) == 5 and len(o&input_data_map[4]) == 2:
                translated_number += '2'
            elif len(o) == 5 and len(o&input_data_map[4]) == 3 and len(o&input_data_map[2]) == 1:
                translated_number += '5'
            elif len(o) == 5 and len(o&input_data_map[4]) == 3 and len(o&input_data_map[2]) == 2:
                translated_number += '3'
            elif len(o) == 6 and len(o&input_data_map[4]) == 4:
                translated_number += '9'
            elif len(o) == 6 and len(o&input_data_map[4]) == 3 and len(o&input_data_map[2]) == 1:
                translated_number += '6'
            elif len(o) == 6 and len(o&input_data_map[4]) == 3 and len(o&input_data_map[2]) == 2:
                translated_number += '0'
            
        print(translated_number)
        sum += int(translated_number)
    
    print(sum)