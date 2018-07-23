import arcade


def main():
    arcade.open_window(800, 600, "Drawing Example")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.start_render()
    arcade.draw_arc_filled(150, 144, 15, 36, arcade.color.BOTTLE_GREEN, 90, 360, 45)
    color = (255, 0, 0, 50)
    arcade.draw_arc_filled(150, 154, 15, 36, color, 90, 360, 45)
    arcade.finish_render()
    arcade.pause(4)
    # arcade.close_window()

if __name__ == '__main__':
    main()
