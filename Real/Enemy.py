import arcade


class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visible = True

    def draw(self):
        if self.visible:
            arcade.draw_rectangle_filled(self.x, self.y, 20, 20, arcade.color.RED)

    def update(self, x, y):
        self.x = x
        self.y = y
