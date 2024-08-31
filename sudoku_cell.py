from tkinter import *
CELL_HEIGHT=38
CELL_WIDTH=38
TEXT_HEIGHT=1
TEXT_WIDTH=1
NUMBER_FONT=("Arial",20)

class SudokuCell:
    def __init__(self,block_no:int,row:int,col:int,position:tuple,command) -> None:

        self.block=block_no
        self.row=row
        self.column=col
        self.position=position
        self.button=Button(image=None,  # Initial image can be None or a default image
                           command=lambda r=row, c=col, b=block_no, p=position: command(r,c,b,p),
                           width=CELL_WIDTH,height=CELL_HEIGHT,
                           bg="#FDFDFD")
    
    def change_to_number(self,num):
        self.text=Label(text=num,font=NUMBER_FONT,height=TEXT_HEIGHT,width=TEXT_WIDTH,highlightthickness=0, bd=0,bg="white")
   