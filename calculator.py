import customtkinter as ctk
from settings import *

class Calculator(ctk.CTk):
    def __init__(self, is_dark):
        # setup
        super().__init__(fg_color = (WHITE, BLACK))
        ctk.set_appearance_mode('dark' if is_dark else 'light')    # Sets theme to dark mode or light mode depending on the var is_dark
        self.title('')
        self.iconbitmap('empty.ico')                               # Hides title info
        self.geometry(f'{APP_SIZE[0]}x{APP_SIZE[1]}')
        self.resizable(False, False)                               # Disables resizing and sets window size based on APP_SIZE from settings

        self.mainloop()

if __name__ == '__main__':
    Calculator(DARK_MODE)