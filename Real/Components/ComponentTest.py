import arcade
from arcade.key import *
from Constants import *

class ComponentTest(arcade.Window):
    def __init__(self, obj):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Test")
        self.obj = obj
        self.pressed = []
        self.x = obj.x
        self.y = obj.y

    def on_draw(self):
        arcade.start_render()
        self.obj.draw()
        arcade.draw_text("(%d, %d)" % (self.x, self.y), 10, 10, arcade.color.BLACK)

    def on_key_press(self, symbol: int, modifiers: int):
        self.pressed.append(symbol)

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol in self.pressed:
            self.pressed.remove(symbol)

    def on_update(self, delta_time: float):
        if UP in self.pressed:
            self.y += 1
        if DOWN in self.pressed:
            self.y -= 1
        if LEFT in self.pressed:
            self.x -= 1
        if RIGHT in self.pressed:
            self.x += 1

        self.obj.x = self.x
        self.obj.y = self.y

if __name__ == "__main__":
    from Components.Gauge import Gauge
    ComponentTest(Gauge(0, 0, SCREEN_WIDTH / 8, SCREEN_HEIGHT / 48))
    arcade.set_background_color(arcade.color.WHITE)
    arcade.run()