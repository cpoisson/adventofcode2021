# AOC 2021 Day 01

def increase_count(values):
    count = 0
    for i in range(1, len(values)):
        if values[i] > values[i-1]: count +=1
    return count

with open('day01.input') as f:
    input = [int(x) for x in f.readlines()]

# Part 1
print(increase_count(input))

# Part 2
print(increase_count(
    [sum(input[(i-2):(i+1)]) for i in range(2, len(input))]
    ))