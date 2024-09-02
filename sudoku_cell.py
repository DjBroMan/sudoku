from tkinter import *
CELL_HEIGHT=38
CELL_WIDTH=38
TEXT_HEIGHT=1
TEXT_WIDTH=1
NUMBER_FONT=("Arial",20)

class SudokuCell:
    def __init__(self, block_no: int, row: int, col: int, position: tuple, command) -> None:
        """
        Initialize a SudokuCell with specified block number, row, column, position, and command.

        :param block_no: The block index of the cell.
        :param row: The row index of the cell.
        :param col: The column index of the cell.
        :param position: The (x, y) position of the cell on the grid.
        :param command: The command function to be executed on button click.
        """

        self.block=block_no
        self.row=row
        self.column=col
        self.position=position
        self.button=Button(image=None,  # Initial image can be None or a default image
                           command=lambda r=row, c=col, b=block_no: command(r,c,b),
                           width=CELL_WIDTH,height=CELL_HEIGHT,
                           bg="#FDFDFD")
    
    def change_to_number(self, num: int) -> None:
        """
        Change the cell's display to show the specified number.

        :param num: The number to display in the cell.
        """
        self.text=Label(text=num,font=NUMBER_FONT,height=TEXT_HEIGHT,width=TEXT_WIDTH,highlightthickness=0, bd=0,bg="white")
   