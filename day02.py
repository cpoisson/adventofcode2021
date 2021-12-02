# AOC 2021 Day 02
def decode_instruction(x):
    if x[0] == "forward":
        return [0, int(x[1])]
    elif x[0] == "up":
        return [-1, int(x[1])]
    elif x[0] == "down":
        return [1, int(x[1])]
    else: # invalid
        return [0, 0]

with open('day02.input') as f:
    input = [x.split() for x in f.readlines()]

# Part 1
h = sum(i[1] for i in [decode_instruction(x) for x in input] if i[0] == 0)
d = sum(i[0] * i[1] for i in [decode_instruction(x) for x in input])
print(h*d)

# Part 2
h = sum(i[1] for i in [decode_instruction(x) for x in input] if i[0] == 0)
d = 0
aim = 0
for i in [decode_instruction(x) for x in input]:
    aim += i[0] * i[1]
    if i[0] == 0:
        d += aim * i[1]
print(h*d)