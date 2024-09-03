from sudoku_mechanism import SudokuMechanism
import os

#use this file to make more sudoku questions
#to increase or decrease the numbers given go to sudoku_mechanism and change the NO_TO_SHOW constant to your desired no

def format_sudoku(arr):
    formatted_line=""
    for h in range(0, 9, 3):
        for i in range(3):
            line = []
            for j in range(3):
                one_section=""
                for k in range(3):
                    one_section+=str(arr[j + h][i][k])
                line.append(one_section)
                print(one_section)
            for section in line[:-1]:
                formatted_line+=section+' '
            formatted_line+=line[-1]+'\n'
        formatted_line+='\n'
    print(formatted_line)
    return formatted_line

def create_new_question(question:list,solution:list)->None:
    no_of_questions=len(os.listdir("Sudoku question"))
    new_question=f"Sudoku question/question_{no_of_questions+1}"
    os.mkdir(new_question)
    # os.mkdir(f"Sudoku question/question_{no_of_questions+1}/question.txt")
    # os.mkdir(f"Sudoku question/question_{no_of_questions+1}/solution.txt")

    #Not done
    with open(new_question+"/question.txt","w") as file:
        file.write(format_sudoku(question))
        
    with open(new_question+"/solution.txt","w") as file:
        file.write(format_sudoku(solution))

mechanism=SudokuMechanism()
mechanism.generate_complete_sudoku()
mechanism.generate_question()

create_new_question(mechanism.sudoku,mechanism.ans_sudoku)


    


        

    
test_sudoku = [[[0, 3, 0], [0, 0, 7], [9, 0, 0]], [[0, 8, 0], [4, 0, 1], [0, 5, 0]], [[0, 0, 1], [0, 5, 0], [2, 0, 0]], [[0, 0, 2], [3, 0, 0], [5, 9, 0]], [[0, 0, 5], [2, 1, 0], [0, 6, 0]], [[0, 1, 0], [5, 0, 0], [0, 0, 2]], [[0, 0, 6], [0, 0, 9], [0, 0, 0]], [[5, 0, 2], [6, 0, 0], [0, 0, 8]], [[0, 0, 0], [0, 2, 7], [0, 6, 5]]]
test_sudoku_2 = [[[0, 3, 0], [0, 0, 7], [9, 0, 1]], [[0, 8, 0], [4, 0, 1], [0, 5, 0]], [[0, 0, 1], [0, 5, 0], [2, 0, 0]], [[0, 0, 2], [3, 0, 0], [5, 9, 0]], [[0, 0, 5], [2, 1, 0], [0, 6, 0]], [[0, 1, 0], [5, 0, 0], [0, 0, 2]], [[0, 0, 6], [0, 0, 9], [0, 0, 0]], [[5, 0, 2], [6, 0, 0], [0, 0, 8]], [[0, 0, 0], [0, 2, 7], [0, 6, 5]]]

create_new_question(test_sudoku,test_sudoku_2)