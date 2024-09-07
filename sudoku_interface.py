from tkinter import *
from sudoku_cell import SudokuCell
from sudoku_mechanism import SudokuMechanism
from helpful_functions import get_no_of_blanks, display
import copy

BLOCK_HEIGHT=141
BLOCK_WIDTH=147
CELL_HEIGHT=38
CELL_WIDTH=38
X_SHIFT=48
Y_SHIFT=46
NUMBER_FONT=("Arial",10)
SUDOKU_FONT=("Arial",40,"bold")

def check_button_image(button:Button, image_to_check):
    """
    Check if the image in the given button matches the specified image.

    :param button: The Button widget to check.
    :param image_to_check: The PhotoImage object to compare against.
    :return: True if the button's image matches the specified image, False otherwise.
    """
    button_image = button.cget('image')  # Retrieve the image set on the button

    # Check if the image matches
    return button_image == str(image_to_check)  # Convert image to string for comparison

class SudokuInterface:
    def __init__(self,difficulty:str,question_no:int) -> None:
        """
        Initialize the SudokuInterface, setting up the window, images, and Sudoku grid.
        """
        #Controls
        self.is_sudoku_button_clicked=False
        self.selected_button=None
        self.mechanism=SudokuMechanism(difficulty=difficulty,q_no=question_no)
        self.mechanism.set_data()

        #Window
        self.window=Tk()
        self.window.geometry("500x620")  # Set a window size for better placement control
        self.window.title("Sudoku")

        #Images
        self.white_background=PhotoImage(file="images/White background.png")
        self.green_background=PhotoImage(file="images/green_background.png")
        self.red_background=PhotoImage(file="images/red_background.png")
    #The Word Sudoku
        self.sudoku_test_box=Label(text="Sudoku",font=SUDOKU_FONT)
        self.sudoku_test_box.grid(row=0,column=0,pady=0)

    #Sudoku Display
        self.sudoku_canvas_display=Canvas(width=453,height=435)
        blank_sudoku=PhotoImage(file="images/sudoku-blankgrid.png")
        self.sudoku_canvas_display.create_image(222,218,image=blank_sudoku)

        # Place the sudoku canvas using grid
        self.sudoku_canvas_display.grid(row=1, column=0, padx=20, pady=20)


        #buttons for selecting cell
        self.all_buttons=[[],[],[],[],[],[],[],[],[]]
        self.position_of_buttons=[[],[],[],[],[],[],[],[],[]]
        
        block_no=0
        for height_multiplier in range(3):
            for width_multiplier in range(3):
                h=height_multiplier*BLOCK_HEIGHT
                w=width_multiplier*BLOCK_WIDTH
                y=0
                for row in range(3):
                    self.all_buttons[block_no].append([])  
                    self.position_of_buttons[block_no].append([])  
                    x=0
                    for col in range(3):
                        position=(5+x+w,10+y+h)
                        self.position_of_buttons[block_no][row].append(position)
                        new_cell=SudokuCell(block_no=block_no,row=row,col=col,command=self.button_click,position=position)
                        new_cell.button.config(image=self.white_background)
                        self.all_buttons[block_no][row].append(new_cell)
                        self.button_canvas=self.sudoku_canvas_display.create_window(position,anchor="nw",window=new_cell.button)
                        x+=X_SHIFT
                    y+=Y_SHIFT
                block_no+=1

    # Number Display
        self.number_display=Canvas(height=100,width=453)
        self.number_display.place(x=45, y=570)  # Position below the Sudoku canvas
        self.number_buttons={}
        x=0
        for num in range(1,10):
            button=Button(text=num,command=lambda n=num:self.replace_with_number(n),padx=10,pady=10,font=NUMBER_FONT)
            self.number_buttons[num]=button
            self.number_canvas=self.number_display.create_window(5+x,0,window=button)
            x+=48
        
        #Setting Data
        for b in range(9):
            for r in range(3):
                for c in  range(3):
                    if self.mechanism.sudoku[b][r][c]!=0:
                        cell=self.all_buttons[b][r][c]
                        cell.button.destroy()
                        cell.change_to_number(self.mechanism.sudoku[b][r][c])
                        self.button_canvas=self.sudoku_canvas_display.create_window(cell.position[0]+13,cell.position[1]+5,anchor="nw",window=cell.text)
        
        self.mechanism.copy_sudoku=copy.deepcopy(self.mechanism.sudoku)


        
        self.window.mainloop()

    def button_click(self, r: int, c: int, b: int) -> None:
        """
        Handle the event when a Sudoku cell button is clicked.

        :param r: The row index of the clicked cell.
        :param c: The column index of the clicked cell.
        :param b: The block index of the clicked cell.
        """
        # print(f"block {b}, row {r}, column {c}")
        if check_button_image(self.all_buttons[b][r][c].button,self.white_background):
            self.turn_all_display_buttons_white()
            if not self.is_sudoku_button_clicked:
                self.is_sudoku_button_clicked=True

            self.all_buttons[b][r][c].button.config(image=self.green_background)
            self.selected_button=self.all_buttons[b][r][c]
        else:
            self.all_buttons[b][r][c].button.config(image=self.white_background)
            self.selected_button=None
        # print(f"{self.selected_button}")
            
    #going to act like a submit button
    def replace_with_number(self, num: int) -> None:
        """
        Replace the selected cell with the specified number.

        :param num: The number to place in the selected cell.
        """
        # print(f"number is {num}")
        # print(self.is_sudoku_button_clicked)
        # print(self.selected_button)
        if self.is_sudoku_button_clicked and self.selected_button:
            b=self.selected_button.block
            r=self.selected_button.row
            c=self.selected_button.column
            # print("a")
            if self.mechanism.add_number(num,b,r,c):
                # display(self.mechanism.ans_sudoku)
                # display(self.mechanism.sudoku)
                cell = self.all_buttons[b][r][c]
                cell.button.destroy()
                cell.change_to_number(num)
                self.button_canvas=self.sudoku_canvas_display.create_window(cell.position[0]+13,cell.position[1]+5,anchor="nw",window=cell.text)
                # print("b")
                self.check_game_end()
            else:
                self.all_buttons[b][r][c].button.config(image=self.red_background)
                self.is_sudoku_button_clicked=False
                self.selected_button=None
                # print("c")      
        self.disable_complete_numbers()                     

    def turn_all_display_buttons_white(self) -> None:
        """
        Reset the image of all Sudoku cell buttons to the white background.
        """
        for block in self.all_buttons:
            for row in block:
                for cell in row:
                    try:
                        cell.button.config(image=self.white_background)
                    except:
                        pass

    def check_game_end(self) -> None:
        """
        Check if the Sudoku game has ended (i.e., no blanks are left).
        """
        if get_no_of_blanks(self.mechanism.sudoku)==0:
            print("Game End")

    def disable_complete_numbers(self)->None:
        """
        disables the number buttons which have been filled (i.e appeared 9 times)
        """

        list_of_numbers=self.mechanism.find_all_complete_numbers()
        for num in list_of_numbers:
            self.number_buttons[num].config(state=DISABLED)

        