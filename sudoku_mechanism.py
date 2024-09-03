from helpful_functions import *
import copy
from random import randint, shuffle

#the print statements are used for debugging
#to play another sudoku change the question no

QUESTION_NO=6
NO_TO_SHOW=30



class SudokuMechanism:
    def __init__(self) -> None:
        """
        Initialize the SudokuMechanism with empty grids for sudoku, copy_sudoku, and ans_sudoku.
        """
        #              row                    column                 block
        self.sudoku=[[[0 for _ in range(3)] for _ in range(3)] for _ in range(9)]
        #                    row                    column                 block
        self.copy_sudoku=[[[0 for _ in range(3)] for _ in range(3)] for _ in range(9)]
        #                    row                    column                 block
        self.ans_sudoku=[[[0 for _ in range(3)] for _ in range(3)] for _ in range(9)]
    
    def set_data(self) -> None:
        """
        Set the Sudoku puzzle and its solution from files.
        """
        with open(f"Sudoku question/question_{QUESTION_NO}/question.txt") as question:
            for coef in range(3):
                l=3*coef
                for i in range(3):
                    line=question.readline().split('\n')[0]
                    data=line.split()
                    for j in range(3):
                        for k in range(3):
                            self.sudoku[j+l][i][k]=int(data[j][k])
                trash=question.readline()
        self.copy_sudoku = copy.deepcopy(self.sudoku)

        with open(f"Sudoku question/question_{QUESTION_NO}/solution.txt") as question:
            for coef in range(3):
                l=3*coef
                for i in range(3):
                    line=question.readline().split('\n')[0]
                    data=line.split()
                    for j in range(3):
                        for k in range(3):
                            self.ans_sudoku[j+l][i][k]=int(data[j][k])
                trash=question.readline()

    def generate_complete_sudoku(self) -> None:
        """
        Generate a complete Sudoku puzzle and save the solution.
        """
        # Start the backtracking process
        self.fill_grid(0, 0)
        self.ans_sudoku = copy.deepcopy(self.sudoku)  # Save the solution
        
    def fill_grid(self, row: int, col: int) -> bool:
        """
        Fill the Sudoku grid using a backtracking algorithm.

        :param row: The current row to fill.
        :param col: The current column to fill.
        :return: True if the grid was successfully filled, False otherwise.
        """
        # Move to the next row if we reached the end of the current row
        if col == 9:
            col = 0
            row += 1
            # If we filled all rows, we are done
            if row == 9:
                return True
        
        # Try to fill the current cell
        numbers = list(range(1, 10))
        shuffle(numbers)  # Randomly shuffle numbers to try different combinations
        
        for num in numbers:
            if self.is_safe(num, row, col):
                # Place the number and move to the next cell
                block = (row // 3) * 3 + (col // 3)
                block_row = row % 3
                block_col = col % 3
                self.sudoku[block][block_row][block_col] = num
                
                if self.fill_grid(row, col + 1):
                    return True
                
                # If no valid number was found, reset the cell
                self.sudoku[block][block_row][block_col] = 0
        
        return False

    def is_safe(self, num: int, row: int, col: int) -> bool:
        """
        Check if a number can be safely placed in the specified cell.

        :param num: The number to check.
        :param row: The row index of the cell.
        :param col: The column index of the cell.
        :return: True if the number is safe to place, False otherwise.
        """
        # Check if num is not present in the current row, column, or block
        block = (row // 3) * 3 + (col // 3)
        block_row = row % 3
        block_col = col % 3
        
        # Temporarily place the number in the cell
        self.sudoku[block][block_row][block_col] = num
        
        # Check for repetition using the provided functions
        if is_repetition(self.sudoku):
            self.sudoku[block][block_row][block_col] = 0
            return False
        
        # No repetition found, the number is safe to place
        self.sudoku[block][block_row][block_col] = 0
        return True
  
    def compare_with_answer(self) -> bool:
        """
        Compare the current Sudoku puzzle with the solution to check if it's correct.

        :return: True if the current puzzle matches the solution, False otherwise.
        """
        # print("copy sudoku-")
        # display(self.copy_sudoku)
        for i in range(9):
            for j in range(3):
                for k in range(3):
                    temp = self.copy_sudoku[i][j][k]
                    if temp != 0:
                        # print(f"temp- {temp}") 
                        if self.ans_sudoku[i][j][k] != temp:
                            # print("Wrong answer")
                            # print(f"ans- {self.ans_sudoku[i][j][k]}")
                            return False
        # print(f"temp- {temp}") 
        # print(f"ans- {self.ans_sudoku[i][j][k]}")
        return True
    
    def add_number(self, num: int, block: int, row: int, col: int) -> bool:
        """
        Add a number to the Sudoku grid and check if the current state is valid.

        :param num: The number to add.
        :param block: The block index of the cell.
        :param row: The row index of the cell.
        :param col: The column index of the cell.
        :return: True if the number was added successfully and the state is valid, False otherwise.
        """
        self.copy_sudoku[block][row][col]=num
        # print("in add number")
        if is_repetition(self.copy_sudoku):
            self.copy_sudoku=copy.deepcopy(self.sudoku)
            return False
            
        else:
            if self.compare_with_answer():
                self.sudoku=copy.deepcopy(self.copy_sudoku)
                return True
            else:
                self.copy_sudoku=copy.deepcopy(self.sudoku)
                return False
    
    def generate_question(self):
        self.copy_sudoku=deepcopy(self.sudoku)
        count=81-NO_TO_SHOW
        while count>0:
            b=randint(0,8)
            r=randint(0,2)
            c=randint(0,2)
            if self.copy_sudoku[b][r][c] != 0:
                self.copy_sudoku[b][r][c]=0
                temp=solve_sudoku(self.copy_sudoku)
                if temp==self.ans_sudoku:
                    display(self.copy_sudoku)
                    count-=1
                else:
                    self.copy_sudoku[b][r][c]=self.sudoku[b][r][c]
        self.sudoku=deepcopy(self.copy_sudoku)


