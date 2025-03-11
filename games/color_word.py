"""
Instructions: Type the displayed color to win!
"""

''' 
TODO: 
    - create ongoing engagement with new word after each submission
    - timer for each user guess
    - use point system
    - import fonts to bold displayword for visibility purposes
    - center all items in the window
'''


import dearpygui.dearpygui as dpg
import random

# color names to RGB values
correct_colors = {
    "Red": (255, 0, 0),
    "Green": (0, 255, 0),
    "Blue": (0, 0, 255),
    "Yellow": (255, 255, 0),
    "Purple": (128, 0, 128),
    "Orange": (255, 165, 0),
}


def check_guess(correct_word, parent):
    """
    Compare user guess with the correct word.
    :param correct_word:
    :param parent: mount to main window
    :return: None
    """
    user_guess = dpg.get_value("guess_input")
    if user_guess.lower() == correct_word.lower():
        dpg.add_text("Correct!", color=(0, 255, 0), parent=parent)
    else:
        dpg.add_text(f"Wrong! The correct color was {correct_word}.", color=(255, 0, 0), parent=parent)


def start_game(parent_window):
    display_word = random.choice(list(correct_colors.keys()))

    correct_word, display_rgb = random.choice(
        [(name, rgb) for name, rgb in correct_colors.items() if name != display_word]
    )

    dpg.add_text("Guess the color of the word:", parent=parent_window)
    dpg.add_text(f"Word: {display_word}", color=display_rgb, parent=parent_window)

    with dpg.group(parent=parent_window):
        dpg.add_input_text(tag="guess_input", on_enter=True, callback=lambda: check_guess(correct_word, parent_window))
        # dpg.add_button(label="Submit", callback=lambda: check_guess(correct_word, parent_window))

