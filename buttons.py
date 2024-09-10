from customtkinter import CTkButton
from settings import *

class Button(CTkButton):
    def __init__(self, parent, text, func, col, row, font, span = 1, color = 'dark-gray'):
        super().__init__(
            parent, 
            command = func,
            text = text,
            font = font,
            corner_radius = STYLING['corner-radius'],
            fg_color = COLORS[color]['fg'],
            hover_color = COLORS[color]['hover'],
            text_color = COLORS[color]['text'])
        self.grid(column = col, row = row, sticky = 'news', padx = STYLING['gap'], pady = STYLING['gap'], columnspan = span)

class NumButton(Button):
    def __init__(self, parent, text, func, col, row, font, span, color = 'light-gray'):
        super().__init__( 
            parent = parent, 
            text = text, 
            func = lambda: print(text), 
            col = col, 
            row = row, 
            font = font, 
            color = color,
            span = span)