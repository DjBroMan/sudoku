import copy

#the print statements are used for debugging
#to play another sudoku change the question no

QUESTION_NO=1

def has_duplicates(vec):
    seen = set()
    for num in vec:
        if num != 0:
            if num in seen:
                return True  # Duplicate found
            seen.add(num)
    return False  # No duplicates

#For debuging
def display(vec):
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

class SudokuMechanism:
    def __init__(self) -> None:
        #              row                    column                 block
        self.sudoku=[[[0 for _ in range(3)] for _ in range(3)] for _ in range(9)]
        #                    row                    column                 block
        self.copy_sudoku=[[[0 for _ in range(3)] for _ in range(3)] for _ in range(9)]
        #                    row                    column                 block
        self.ans_sudoku=[[[0 for _ in range(3)] for _ in range(3)] for _ in range(9)]
    
    def set_data(self):
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
    
    def get_no_of_blanks(self):
        blanks=0
        for b in range(9):
            for r in range(3):
                for c in range(3):
                    if self.sudoku[b][r][c]==0:
                        blanks+=1
        return blanks

    def is_repetition(self):
        if self.block_repetition():
            print("Repetition in the block")
            print("copy sudoku-")
            display(self.copy_sudoku)
            return True
        elif self.row_repetition():
            print("Repetition in the row")
            return True
        elif self.column_repetition():
            print("Repetition in the column")
            return True
        else:
            return False

    def block_repetition(self):
        check = 1
        for i in range(9):
            vec = []
            for j in range(3):
                for k in range(3):
                    vec.append(self.copy_sudoku[i][j][k])
            if has_duplicates(vec):
                # print(f"Repetition in the block {check}")
                return True
            else:
                check += 1
        # print("No repetition in blocks")
        return False

    def row_repetition(self):
        check = 1
        for h in range(0, 9, 3):
            for i in range(3):
                vec = []
                for j in range(3):
                    for k in range(3):
                        vec.append(self.copy_sudoku[j + h][i][k])
                if has_duplicates(vec):
                    # print(f"Repetition in the row {check}")
                    return True
                else:
                    check += 1
        # print("No repetition in rows")
        return False

    def column_repetition(self):
        check = 1
        for j in range(3):
            for i in range(3):
                vec = []
                for h in range(0, 9, 3):
                    for k in range(3):
                        vec.append(self.copy_sudoku[h + j][k][i])
                if has_duplicates(vec):
                    # print(f"Repetition in the column {check}")
                    return True
                else:
                    check += 1
        # print("No repetition in columns")
        return False

    def compare_with_answer(self):
        print("copy sudoku-")
        display(self.copy_sudoku)
        for i in range(9):
            for j in range(3):
                for k in range(3):
                    temp = self.sudoku[i][j][k]
                    if temp != 0:
                        if self.ans_sudoku[i][j][k] != temp:
                            print("Wrong answer")
                            print(f"temp- {temp}") 
                            print(f"ans- {self.ans_sudoku[i][j][k]}")
                            return False
        print(f"temp- {temp}") 
        print(f"ans- {self.ans_sudoku[i][j][k]}")
        return True
    
    def add_number(self,num,block,row,col):
        self.copy_sudoku[block][row][col]=num
        print("in add number")
        if self.is_repetition():
            self.copy_sudoku=copy.deepcopy(self.sudoku)
            return False
            
        else:
            if self.compare_with_answer():
                self.sudoku=copy.deepcopy(self.copy_sudoku)
                return True
            else:
                self.copy_sudoku=copy.deepcopy(self.sudoku)
                return False