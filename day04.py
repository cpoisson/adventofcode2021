# AOC 2021 Day 04

with open('day04.input') as f:
    input = [x.strip() for x in f.readlines() if len(x.strip()) > 0]

numbers = [int(x) for x in input[0].split(',')]
boards_lines = [[int(y) for y in x.split()] for x in input[1:]]
boards = [boards_lines[i * 5: (i + 1) * 5] for i in range(0, len(boards_lines)/5)]

def is_winning(board, drawn_nums):
    for line in board:
        if set(line).issubset(set(drawn_nums)):
            return True
    for j in range(len(board[0])):
        if set([line[j] for line in board]).issubset(set(drawn_nums)):
            return True
    return False

def find_winning_boards(boards):
    winning_boards = list()
    for draw_turn in range(len(numbers)):
        for board in boards:
            if is_winning(board, numbers[:draw_turn]):
                winning_boards.append([board, draw_turn])
                boards.remove(board)
    return winning_boards

winning_boards = find_winning_boards(boards)

# Part 01

winning_board = winning_boards[0][0]
draw_turn = winning_boards[0][1]

print(numbers[:draw_turn][-1] * sum([num for line in winning_board for num in line if num not in numbers[:draw_turn]]))

# Part 02

last_winning_board = winning_boards[-1][0]
draw_turn = winning_boards[-1][1]

print(numbers[:draw_turn][-1] * sum([num for line in last_winning_board for num in line if num not in numbers[:draw_turn]]))
