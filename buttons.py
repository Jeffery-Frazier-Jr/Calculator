from customtkinter import CTkButton
from settings import *

class Button(CTkButton):
    def __init__(self, parent, text, func, col, row, font, color = 'dark-gray'):
        super().__init__(
            parent, 
            command = func,
            text = text,
            font = font,
            corner_radius = STYLING['corner-radius'],
            fg_color = COLORS[color]['fg'],
            hover_color = COLORS[color]['hover'],
            text_color = COLORS[color]['text'])
        self.grid(column = col, row = row, sticky = 'news', padx = STYLING['gap'], pady = STYLING['gap'])