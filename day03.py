# AOC 2021 Day 03

with open('day03.input') as f:
    input = [x.strip() for x in f.readlines()]

test_input = [
    '00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010'
]

# Part 1

gamma_rate = ''
for i in range(len(input[0])):
    gamma_rate += '1' if sum([int(binary[i]) for binary in input]) > len(input) / 2 else '0'

print(int(gamma_rate, base=2) * (int(gamma_rate, base=2) ^ int('1'*len(gamma_rate), base=2)))

# Part 2

def o2_generator_rating(binaries, i):
    criteria = '1' if sum([int(binary[i]) for binary in binaries]) >= len(binaries)/2 else '0'
    binaries = [binary for binary in binaries if binary[i] == criteria]
    i += 1
    return int(binaries[0], base=2) if len(binaries) == 1 else o2_generator_rating(binaries, i)

def co2_scrubber_rating(binaries, i):
    criteria = '0' if sum([int(binary[i]) for binary in binaries]) >= len(binaries)/2 else '1'
    binaries = [binary for binary in binaries if binary[i] == criteria]
    i += 1
    return int(binaries[0], base=2) if len(binaries) <= 1 else co2_scrubber_rating(binaries, i)

print(o2_generator_rating(input, 0) * co2_scrubber_rating(input, 0))