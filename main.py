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


def valid_change(matrix: list, row: int, col: int, value: int, user: bool):
    for i in range(0, 9):
        if matrix[i][col - 1] == value:
            if user:
                print("Value Already being used in that Collum")
            return False
        elif matrix[row - 1][i] == value:
            if user:
                print("Value Already being used in that Row")
            return False

    if row < 4:
        temp_row = 0
    elif row < 7:
        temp_row = 3
    else:
        temp_row = 6

    if col < 4:
        temp_col = 0
    elif col < 7:
        temp_col = 3
    else:
        temp_col = 6

    for i in range(0, 3):
        for j in range(0, 3):
            if matrix[temp_row + i][temp_col + j] == value:
                if user:
                    print("Value Already being used in that Section")
                return False

    return True


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


def input_value(matrix: list, user: bool):
    while True:
        col_input = int(input("Input Collum Cell you would like to change 1 to 9: "))
        row_input = int(input("Input Row Cell you would like to change from 1 to 9: "))
        number_input = int(input("Input Number you want to place inside from 1 to 9: "))
        if 0 < row_input < 10 and 0 < col_input < 10 and 0 < number_input < 10 \
                and valid_change(matrix, row_input, col_input, number_input, True):
            break
        else:
            if user:
                print("Invalid Input Please Try Again")
    matrix[row_input - 1][col_input - 1] = number_input

    return matrix


def findNextCell(matrix: list, i, j):
    for m in range(i, 9):
        for n in range(j, 9):
            if matrix[m][n] == -1:
                return m, n

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


def solve_matrix(matrix: list, i=0, j=0):
    i, j = findNextCell(matrix, i, j)
    if i == -2:
        return True
    for m in range(1, 10):
        if isValid(matrix, i, j, m):
            matrix[i][j] = m
            if solve_matrix(matrix, i, j):
                return True
            matrix[i][j] = -1

    return False


def main():
    matrix = create_matrix()
    solve_matrix(matrix)
    print_matrix(matrix)


if __name__ == '__main__':
    main()
