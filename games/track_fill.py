"""
Instructions: navigate the levels to fill all blocks using a single path to win!
"""

''' 

'''


import dearpygui.dearpygui as dpg
import random

def start_game(parent_window):
    dpg.add_text('add a grid')
    with dpg.group(parent=parent_window):
        dpg.add_text('add a grid')
        # dpg.add_button(label="Submit", callback=lambda: check_guess(correct_word, parent_window))

