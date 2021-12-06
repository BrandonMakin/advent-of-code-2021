############################################
# PART 1
############################################

with open("03/input_1.txt") as file:
    bit_length = 12
    line_count = 0
    ones = [0] * bit_length # 12 bits long
    for line in (file):
        line_count += 1
        line = line.strip("\n")
        for i, bit in enumerate(line):
            ones[i] += int(bit)
    
    # assemble results from array of bits
    most_common_bits = [int(one_count * 2 > line_count) for one_count in ones]
    equally_common_bits = [int(one_count * 2 == line_count) for one_count in ones] # added for part 2
    print(ones)
    print(most_common_bits)

    most_common_bits.reverse()
    gamma = 0
    epsilon = 0
    for i, bit in enumerate(most_common_bits):
        gamma += bit << i
        epsilon += (bit != 1) << i

    print(f"""
>>──────────► PART 1 >>───────────►
    Epsilon: {epsilon}
    Gamma: {gamma}
    Result 1 answer: {epsilon * gamma}
>>────────────────────────────────►
""")

############################################
# PART 2
############################################

with open("03/input_1.txt") as file:
    data = file.read().splitlines()

    possible_oxygen_ratings = [r for r in data if int(r[0]) == most_common_bits[0]]
    possible_CO2_ratings = [r for r in data if int(r[0]) != most_common_bits[0]]

    bit_index = 1 # current bit I'm looking at
    while len(possible_oxygen_ratings) > 1 and bit_index <= bit_length:
        number_of_ones_in_this_column = sum(r[bit_index] == "1" for r in possible_oxygen_ratings)
        most_common_bit = int(number_of_ones_in_this_column * 2 >= len(possible_oxygen_ratings))
        possible_oxygen_ratings = [r for r in possible_oxygen_ratings if int(r[bit_index]) == most_common_bit]
        bit_index += 1
    
    oxygen_rating = possible_oxygen_ratings[0]

    bit_index = 1 # current bit I'm looking at
    while len(possible_CO2_ratings) > 1 and bit_index <= bit_length:
        number_of_ones_in_this_column = sum(r[bit_index] == "1" for r in possible_CO2_ratings)
        most_common_bit = int(number_of_ones_in_this_column * 2 >= len(possible_CO2_ratings))
        possible_CO2_ratings = [r for r in possible_CO2_ratings if int(r[bit_index]) != most_common_bit]
        bit_index += 1
    
    C02_rating = possible_CO2_ratings[0]

    oxygen_rating = int(oxygen_rating, 2)
    C02_rating = int(C02_rating, 2)


print(f"""
>>──────────► PART 2 >>───────────►
    Line count: {line_count}
    One count: {ones}
    Equally common bits: {equally_common_bits}
    Most common bits: {most_common_bits}

    Oxygen rating : {oxygen_rating}
    C02 rating : {C02_rating}
    Result: {oxygen_rating * C02_rating}
>>────────────────────────────────►
""")