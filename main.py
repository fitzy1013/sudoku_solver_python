import random


def create_spaces(matrix, level):
    if level == 1:
        spaces = 10
    elif level == 2:
        spaces = 20
    else:
        spaces = 30
    pair_list = []
    for m in range(0, 9):
        for n in range(0, 9):
            pair_list.append([m, n])

    open_spaces = []

    for i in range(0, spaces):
        index = random.randint(0, len(pair_list) - 1)
        matrix[pair_list[index][0]][pair_list[index][1]] = -1
        open_spaces.append([pair_list[index][0], pair_list[index][1]])
        del pair_list[index]

    return open_spaces


def fill_matrix2(matrix):
    i = 0
    j = 0
    i, j = findNextCell(matrix, i, j)
    if i == -2:
        return True
    numbers = create_random_number_list(matrix, i, j)
    random.shuffle(numbers)
    for m in numbers:
        if isValid(matrix, i, j, m, False):
            matrix[i][j] = m
            if fill_matrix2(matrix):
                return True

    matrix[i][j] = -1
    return False


def create_matrix():
    matrix_inner = []
    matrix = []

    for i in range(0, 9):
        if i > 0:
            matrix.append(matrix_inner)
            matrix_inner = []
        for j in range(0, 9):
            matrix_inner.append(-1)

    matrix.append(matrix_inner)

    return matrix


def fill_matrix(matrix: list):
    cells_filled = 0
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while cells_filled < 20:
        temp_number_list = number_list
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if matrix[row][col] == -1:
            while len(temp_number_list) != 0:
                value = random.randint(0, len(temp_number_list) - 1)
                if isValid(matrix, row, col, temp_number_list[value], False):
                    matrix[row][col] = temp_number_list[value]
                    cells_filled += 1
                    break
                else:
                    del temp_number_list[value]


def print_matrix(matrix: list):
    row_number = 1
    col_string = " "
    print("   ", end="")
    for i in range(1, 10):
        if (i - 1) % 3 == 0 and i != 1:
            print("|| " + str(i) + " ", end="")
        else:
            print("| " + str(i) + " ", end="")
    print("\n=============================================")
    for row in matrix:
        if row_number > 1:
            if (row_number - 1) % 3 == 0:
                print("\n===========================================")
            else:
                print("\n-------------------------------------------")

        print(str(row_number) + " |", end="")
        row_number += 1
        col_number = 0
        for col in row:
            if col > 0:
                col_string = str(col)
            else:
                col_string = " "

            if col_number % 3 == 0 and col_number != 0:
                print("|| " + col_string + " ", end="")
            else:
                print("| " + col_string + " ", end="")

            col_number += 1

    print("\n-------------------------------------------")


def isSpaceOpen(open_spaces: list, row: int, col: int):
    if [row, col] in open_spaces:
        return True
    else:
        print("This Space is Not Open")
        return False


def input_value(matrix: list, open_spaces: list):
    while True:
        col_input = int(input("Input Collum Cell you would like to change 1 to 9: ")) - 1
        row_input = int(input("Input Row Cell you would like to change from 1 to 9: ")) - 1
        number_input = int(input("Input Number you want to place inside from 1 to 9: "))
        if -1 < row_input < 9 and -1 < col_input < 9 and 0 < number_input < 10 \
                and isValid(matrix, row_input, col_input, number_input, True) \
                and isSpaceOpen(open_spaces, row_input, col_input):
            break
        else:
            print("Invalid Input Please Try Again")
    matrix[row_input][col_input] = number_input

    return matrix


def findNextCell(matrix: list, i, j):
    for m in range(0, 9):
        for n in range(0, 9):
            if matrix[m][n] == -1:
                return m, n

    return -2, -2


def isValid(matrix, i, j, v, user):
    rowOk = all([v != matrix[i][x] for x in range(9)])
    if not rowOk:
        if user:
            print("Current Number is Already being used in that row")
    else:
        columnOk = all([v != matrix[x][j] for x in range(9)])
        if not columnOk:
            if user:
                print("Current Number is Already being used in that row")
        else:
            # finding the top left x,y co-ordinates of the section containing the i,j cell
            secTopX, secTopY = 3 * (i // 3), 3 * (j // 3)  # floored quotient should be used here.
            for x in range(secTopX, secTopX + 3):
                for y in range(secTopY, secTopY + 3):
                    if matrix[x][y] == v:
                        if user:
                            print("Current Number is Already being used in that section")
                        return False
            return True
    return False


def create_random_number_list(matrix, i, j):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    new_numbers = []
    while len(numbers) != 0:
        if isValid(matrix, i, j, numbers[len(numbers) - 1], False):
            new_numbers.append(numbers[len(numbers) - 1])
        numbers.pop()

    return new_numbers


def solve_matrix(matrix):
    i = 0
    j = 0
    i, j = findNextCell(matrix, i, j)
    if i == -2:
        return True
    numbers = create_random_number_list(matrix, i, j)
    for m in numbers:
        if isValid(matrix, i, j, m, False):
            matrix[i][j] = m
            if solve_matrix(matrix):
                return True
            matrix[i][j] = -1

    return False


def userSolved(matrix: list):
    i, j = findNextCell(matrix, 0, 0)
    if i == -2:
        return False
    else:
        return True


def game():
    print("Welcome to the Sudoku Program")
    matrix = create_matrix()  # creates a blank grid
    fill_matrix2(matrix)  # creates a solved game
    print_matrix(matrix)
    level_input = 0
    while level_input < 1 or level_input > 4:
        level_input = int(input("Please Chose your Level \n\n1. Easy (10 Spaces) \n2. Medium (20 Spaces) "
                                "\n3. Hard (30 Spaces) \n4. Exit Program\n\n"))
        if 0 < level_input < 5:
            break
        else:
            print("Invalid Input Please Try Again")

    if level_input == 4:
        exit(0)
    open_spaces = create_spaces(matrix, level_input)
    while True:
        print_matrix(matrix)
        user_input = int(input("Please Chose an Option \n\n1. Input a Number \n2. Solve Puzzle \n3. Exit Program\n\n"))
        if user_input == 1:
            input_value(matrix, open_spaces)
        elif user_input == 2:
            solve_matrix(matrix)
            print_matrix(matrix)
            break
        elif user_input == 3:
            break


def main():
    game()


if __name__ == '__main__':
    main()