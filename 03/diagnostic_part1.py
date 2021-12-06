def get_bit(string, bit_position):
    return string[bit_position:bit_position+1]

with open('input.txt') as f:
    lines = f.readlines()

    gamma = ""
    epsilon = ""

    for i in range(len(lines[0]) - 1):

        zero = 0
        one = 0

        bit_list = map(lambda line: get_bit(line, i), lines)

        for x in bit_list:
            if x == "0":
                zero += 1
            else:
                one += 1

        if zero < one:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"
    
    print(gamma, epsilon)

    gamma_dec = int(gamma, 2)
    epsilon_dec = int(epsilon, 2)

    print(gamma_dec, epsilon_dec)

    print(gamma_dec * epsilon_dec)