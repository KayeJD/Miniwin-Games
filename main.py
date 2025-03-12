import dearpygui.dearpygui as dpg
from games import color_word, track_fill

def main():
    dpg.create_context()
    dpg.create_viewport(title='MiniWin Games :D', width=900, height=700, min_width=900, min_height=600)
    dpg.setup_dearpygui()

    def open_game(game_function):
        """Opens a new child window for the selected game."""
        with dpg.window(label="Game Window", modal=True, width=600, height=400) as game_window:
            game_function(game_window)  # Call the game function inside this window

    with dpg.window(tag='main_window', menubar=False):
        dpg.add_text('Select a Game:')
        dpg.add_button(label="Color Word", callback=lambda: open_game(color_word))
        dpg.add_button(label="Track Fill!", callback=lambda: open_game(track_fill))

    dpg.show_viewport()
    dpg.set_primary_window('main_window', True)

    while dpg.is_dearpygui_running():
        dpg.render_dearpygui_frame()

    dpg.destroy_context()

if __name__ == '__main__':
    main()
