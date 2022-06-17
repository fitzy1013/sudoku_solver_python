import random


def fill_matrix2(matrix):
    i = 0
    j = 0
    i, j = findNextCell(matrix, i, j)
    if i == -2:
        return True
    numbers = create_random_number_list()
    for m in range(0, 9):
        if isValid(matrix, i, j, numbers[m]):
            matrix[i][j] = numbers[m]
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
                if isValid(matrix, row, col, temp_number_list[value]):
                    matrix[row][col] = temp_number_list[value]
                    cells_filled += 1
                    break
                else:
                    del temp_number_list[value]


def print_matrix(matrix: list):
    col_string = " "
    for row in matrix:
        print("\n-------------------------------------------")
        for col in row:
            if col > 0:
                col_string = str(col)
            else:
                col_string = " "
            print("| " + col_string + " ", end="")

    print("\n-------------------------------------------")


def input_value(matrix: list):
    while True:
        col_input = int(input("Input Collum Cell you would like to change 1 to 9: "))
        row_input = int(input("Input Row Cell you would like to change from 1 to 9: "))
        number_input = int(input("Input Number you want to place inside from 1 to 9: "))
        if 0 < row_input < 10 and 0 < col_input < 10 and 0 < number_input < 10 \
                and isValid(matrix, row_input, col_input, number_input):
            break
        else:
            print("Invalid Input Please Try Again")
    matrix[row_input - 1][col_input - 1] = number_input

    return matrix


def findNextCell(matrix: list, i, j):
    for m in range(0, 9):
        for n in range(0, 9):
            if matrix[m][n] == -1:
                return m, n

    return -2, -2


def isValid(matrix, i, j, v):
    rowOk = all([v != matrix[i][x] for x in range(9)])
    if rowOk:
        columnOk = all([v != matrix[x][j] for x in range(9)])
        if columnOk:
            # finding the top left x,y co-ordinates of the section containing the i,j cell
            secTopX, secTopY = 3 * (i // 3), 3 * (j // 3)  # floored quotient should be used here.
            for x in range(secTopX, secTopX + 3):
                for y in range(secTopY, secTopY + 3):
                    if matrix[x][y] == v:
                        return False
            return True
    return False


def create_random_number_list():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    new_numbers = []
    while len(numbers) != 0:
        rand_index = random.randint(0, len(numbers) - 1)
        new_numbers.append(numbers[rand_index])
        del numbers[rand_index]

    return new_numbers


def solve_matrix(matrix):
    i = 0
    j = 0
    i, j = findNextCell(matrix, i, j)
    if i == -2:
        return True
    numbers = create_random_number_list()
    for m in range(0, 9):
        if isValid(matrix, i, j, numbers[m]):
            matrix[i][j] = numbers[m]
            if solve_matrix(matrix):
                return True
            matrix[i][j] = -1

    return False


def main():
    matrix = [
        [7, 8, -1, 4, -1, -1, 1, 2, -1],
        [6, -1, -1, -1, 7, 5, -1, -1, 9],
        [-1, -1, -1, 6, -1, 1, -1, 7, 8],
        [-1, -1, 7, -1, 4, -1, 2, 6, 0],
        [-1, -1, 1, -1, 5, -1, 9, 3, -1],
        [9, -1, 4, -1, 6, -1, -1, -1, 5],
        [-1, 7, -1, 3, -1, -1, -1, 1, 2],
        [1, 2, -1, -1, -1, 7, 4, -1, -1],
        [-1, 4, 9, 2, -1, 6, -1, -1, 7]]

    matrix = create_matrix()
    fill_matrix2(matrix)
    print(matrix)


if __name__ == '__main__':
    main()
