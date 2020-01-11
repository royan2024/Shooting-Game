import arcade
from Scene.SceneController import StartScene
from Constants import *

class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Shooting Game")
        self.scene = StartScene()

    def on_draw(self):
        arcade.start_render()
        self.scene.draw()

    def on_update(self, delta_time: float):
        self.scene.update(delta_time)


    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.scene.mouse_position = (x, y)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        self.scene.pressed.append(button)

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        if button in self.scene.pressed:
            self.scene.pressed.remove(button)

    def on_key_press(self, symbol: int, modifiers: int):
        self.scene.pressed.append(symbol)

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol in self.scene.pressed:
            self.scene.pressed.remove(symbol)

    def scene_transition(self, scene):
        self.scene = scene



if __name__ == "__main__":
    Game()
    arcade.set_background_color(arcade.color.WHITE)
    arcade.run()

