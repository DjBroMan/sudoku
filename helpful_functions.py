from copy import deepcopy

def has_duplicates(vec: list) -> bool:
    """
    Check if there are duplicate non-zero values in a list.

    :param vec: The list of numbers to check.
    :return: True if duplicates are found, False otherwise.
    """
    seen = set()
    for num in vec:
        if num != 0:
            if num in seen:
                return True  # Duplicate found
            seen.add(num)
    return False  # No duplicates

#For debuging
def display(vec: list) -> None:
    """
    Display the Sudoku grid in a formatted way.

    :param vec: The 3D list representing the Sudoku grid to display.
    """
    print("\n===========================================================")
    # no_of_blank = 0
    for l in range(0, 9, 3):
        for k in range(3):
            for j in range(3):
                for i in range(3):
                    if vec[j + l][k][i] != 0:
                        print(vec[j + l][k][i], end=' ')
                    else:
                        print("_", end=' ')
                print("  ", end='')
            print()  # Move to the next line after a group of 3x3 blocks
        print()  # Add an extra line after each block of 3 rows
    # return no_of_blank

def is_repetition(arr: list) -> bool:
    """
    Check if there is any repetition in the Sudoku grid.

    :param arr: The 3D list representing the Sudoku grid to check.
    :return: True if any repetition is found, False otherwise.
    """
    if block_repetition(arr):
        # print("Repetition in the block")
        # print("copy sudoku-")
        # display(arr)
        return True
    elif row_repetition(arr):
        # print("Repetition in the row")
        return True
    elif column_repetition(arr):
        # print("Repetition in the column")
        return True
    else:
        return False

def block_repetition(arr: list) -> bool:
    """
    Check for repetition within each 3x3 block of the Sudoku grid.

    :param arr: The 3D list representing the Sudoku grid to check.
    :return: True if repetition is found in any block, False otherwise.
    """
    check = 1
    for i in range(9):
        vec = []
        for j in range(3):
            for k in range(3):
                vec.append(arr[i][j][k])
        if has_duplicates(vec):
            # print(f"Repetition in the block {check}")
            return True
        else:
            check += 1
    # print("No repetition in blocks")
    return False

def row_repetition(arr: list) -> bool:
    """
    Check for repetition within each row of the Sudoku grid.

    :param arr: The 3D list representing the Sudoku grid to check.
    :return: True if repetition is found in any row, False otherwise.
    """
    check = 1
    for h in range(0, 9, 3):
        for i in range(3):
            vec = []
            for j in range(3):
                for k in range(3):
                    vec.append(arr[j + h][i][k])
            if has_duplicates(vec):
                # print(f"Repetition in the row {check}")
                return True
            else:
                check += 1
    # print("No repetition in rows")
    return False

def column_repetition(arr: list) -> bool:
    """
    Check for repetition within each column of the Sudoku grid.

    :param arr: The 3D list representing the Sudoku grid to check.
    :return: True if repetition is found in any column, False otherwise.
    """
    check = 1
    for j in range(3):
        for i in range(3):
            vec = []
            for h in range(0, 9, 3):
                for k in range(3):
                    vec.append(arr[h + j][k][i])
            if has_duplicates(vec):
                # print(f"Repetition in the column {check}")
                return True
            else:
                check += 1
    # print("No repetition in columns")
    return False

def get_no_of_blanks(arr: list) -> int:
    """
    Count the number of blank cells (zeros) in the Sudoku grid.

    :param arr: The 3D list representing the Sudoku grid to check.
    :return: The number of blank cells.
    """
    blanks=0
    for b in range(9):
        for r in range(3):
            for c in range(3):
                if arr[b][r][c]==0:
                    blanks+=1
    return blanks

def check_valid(arr: list, block: int, row: int, column: int) -> bool:
    """
    Check if a cell in the Sudoku grid is blank (i.e., contains a zero).

    :param arr: The 3D list representing the Sudoku grid to check.
    :param block: The block index of the cell.
    :param row: The row index of the cell.
    :param column: The column index of the cell.
    :return: True if the cell is blank, False otherwise.
    """
    if arr[block][row][column]==0:
        return True
    return False

def solve_sudoku(arr):
    
    arr_copy = deepcopy(arr)
    
    # Iterate through all blocks, rows, and columns
    for block in range(9):
        for row in range(3):
            for column in range(3):
                if arr_copy[block][row][column] == 0:  # Find an empty spot
                    # Try numbers 1-9
                    for number in range(1, 10):
                        arr_copy[block][row][column] = number
                        
                        # Check if placing the number causes any repetition
                        if not is_repetition(arr_copy):
                            # Recursively attempt to solve with this new configuration
                            result = solve_sudoku(arr_copy)
                            if result:  # If the result is a valid solution, return it
                                return result
                        
                        # Backtrack by resetting the cell
                        arr_copy[block][row][column] = 0

                    # If no valid number could be placed, return False for backtracking
                    return False

    # If no blanks are left, a solution has been found
    if get_no_of_blanks(arr_copy) == 0:
        return arr_copy
    
    return False  # No solution found
