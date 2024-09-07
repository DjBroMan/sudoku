from sudoku_mechanism import SudokuMechanism
import os

#use this file to make more sudoku questions

def format_sudoku(arr:list)->str:
    """
    Format a 3D list representing a Sudoku puzzle into a string for writing to a file.

    The formatted string will group the Sudoku puzzle into three sections of three rows,
    with blocks of three numbers separated by spaces and groups of rows separated by blank lines.

    :param arr: A 3D list representing the Sudoku puzzle (9 blocks, each containing 3 rows of 3 numbers).
    :return: A formatted string representing the Sudoku puzzle.
    """
    formatted_line=""
    for h in range(0, 9, 3):
        for i in range(3):
            line = []
            for j in range(3):
                one_section=""
                for k in range(3):
                    one_section+=str(arr[j + h][i][k])
                line.append(one_section)
            for section in line[:-1]:
                formatted_line+=section+' '
            formatted_line+=line[-1]+'\n'
        formatted_line+='\n'
    print(formatted_line)
    return formatted_line

def create_new_question(question: list, solution: list,difficulty:str) -> None:
    """
    Create a new folder for the next Sudoku question of appropriate difficulty and write the question and solution to separate text files.

    The folder will be named "question_{next_question_no}" where {next_question_no} is the next available number.
    The files "question.txt" and "solution.txt" will contain the formatted Sudoku puzzle and its solution, respectively.

    :param question: A 3D list representing the Sudoku puzzle question.
    :param solution: A 3D list representing the Sudoku puzzle solution.
    :return: None
    """
    no_of_questions=len(os.listdir(f"Sudoku question/{difficulty}"))
    new_question=f"Sudoku question/{difficulty}/question_{no_of_questions+1}"
    os.mkdir(new_question)
    # os.mkdir(f"Sudoku question/question_{no_of_questions+1}/question.txt")
    # os.mkdir(f"Sudoku question/question_{no_of_questions+1}/solution.txt")

    #Not done
    with open(new_question+"/question.txt","w") as file:
        file.write(format_sudoku(question))
        
    with open(new_question+"/solution.txt","w") as file:
        file.write(format_sudoku(solution))


mechanism=SudokuMechanism(difficulty="HARD")
mechanism.generate_complete_sudoku()
#to increase or decrease the numbers given go to the puzzle change the no inside
mechanism.generate_question()

create_new_question(question=mechanism.sudoku,solution=mechanism.ans_sudoku,difficulty=mechanism.difficulty)
