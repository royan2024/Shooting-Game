import arcade


class Enemy:
    def __init__(self, x, y, size=20):
        self.x = x
        self.y = y
        self.size = size
        self.visible = True

    def draw(self):
        if self.visible:
            arcade.draw_rectangle_filled(self.x, self.y, self.size, self.size, arcade.color.RED)

    def update(self, x, y):
        self.x = x
        self.y = y
