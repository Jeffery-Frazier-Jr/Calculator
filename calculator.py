import customtkinter as ctk
from buttons import Button
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

        # grid layout
        self.rowconfigure(list(range(MAIN_ROWS)), weight = 1, uniform = 'a')
        self.columnconfigure(list(range(MAIN_COLUMNS)), weight = 1, uniform = 'a')

        # data
        self.formula_string = ctk.StringVar(value = '')
        self.result_string = ctk.StringVar(value = '0')

        # widgets
        self.create_widgets()

        self.mainloop()

    def create_widgets(self):
        # fonts
        main_font = ctk.CTkFont(family = FONT, size = NORMAL_FONT_SIZE)
        result_font = ctk.CTkFont(family = FONT, size = OUTPUT_FONT_SIZE)

        # output labels
        OutputLabel(self, 0, 'se', main_font, self.formula_string) # formula
        OutputLabel(self, 1, 'e', result_font, self.result_string) # result

        # clear (AC) button
        Button(
            parent = self,
            func = self.clear, 
            text = OPERATORS['clear']['text'], 
            col = OPERATORS['clear']['col'], 
            row = OPERATORS['clear']['row'],
            font = main_font)
        
        # invert button
        Button(
            parent = self,
            func = self.invert,
            text = OPERATORS['invert']['text'], 
            col = OPERATORS['invert']['col'], 
            row = OPERATORS['invert']['row'],
            font = main_font)
        
        # percentage button
        Button(
            parent = self,
            func = self.percent,
            text = OPERATORS['percent']['text'],
            col = OPERATORS['percent']['col'],
            row = OPERATORS['percent']['row'],
            font = main_font)
        
    def clear(self):
        print('clear')

    def percent(self):
        print('percent')
    
    def invert(self):
        print('+invert-')

class OutputLabel(ctk.CTkLabel):
    def __init__(self, parent, row, anchor, font, string_var):
        super().__init__(parent, font = font, textvariable = string_var)
        self.grid(column = 0, columnspan = 4, row = row, sticky = anchor, padx = 10)

if __name__ == '__main__':
    Calculator(DARK_MODE)