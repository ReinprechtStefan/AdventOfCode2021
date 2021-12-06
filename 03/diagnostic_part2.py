def get_bit(string, bit_position):
    return string[bit_position:bit_position+1]

with open('input.txt') as f:
    lines = f.readlines()
    oxygen_data = lines
    co2_data = lines

    OXYGEN = ""
    CO2 = ""

    for i in range(len(oxygen_data[0]) - 1):
        #print(len(oxygen_data))

        if len(oxygen_data) == 1:
            OXYGEN = oxygen_data[0]
            break

        zero = 0
        one = 0

        bit_list = map(lambda line: get_bit(line, i), oxygen_data)

        for x in bit_list:
            if x == "0":
                zero += 1
            else:
                one += 1

        #print(zero, one)

        if zero == one:
            OXYGEN += "1"
        elif zero < one:
            OXYGEN += "1"
        elif one < zero:
            OXYGEN += "0"

        oxygen_data = list(filter(lambda line: str(line).startswith(OXYGEN), oxygen_data))

    for i in range(len(co2_data[0]) - 1):
        #print(len(co2_data))

        if len(co2_data) == 1:
            CO2 = co2_data[0]
            break

        zero = 0
        one = 0

        bit_list = map(lambda line: get_bit(line, i), co2_data)

        for x in bit_list:
            if x == "0":
                zero += 1
            else:
                one += 1

        if zero == one:
            CO2 += "0"
        elif zero < one:
            CO2 += "0"
        elif one < zero:
            CO2 += "1"

        print(CO2)

        co2_data = list(filter(lambda line: str(line).startswith(CO2), co2_data))
    
    print(OXYGEN, CO2)

    gamma_dec = int(OXYGEN, 2)
    epsilon_dec = int(CO2, 2)

    print(gamma_dec, epsilon_dec)

    print(gamma_dec * epsilon_dec)
        