import arcade

class Gauge:
    def __init__(self, x, y, w, h, fill=1.0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.fill = fill

    def update(self, delta_fill):
        self.fill += delta_fill
        self.fill = max(0, min(1, self.fill))

    def draw1(self):
        shifted_x = self.x - (self.w - self.fill * self.w) / 2
        arcade.draw_rectangle_filled(shifted_x, self.y, self.w * self.fill, self.h, color=arcade.color.AERO_BLUE)
        arcade.draw_rectangle_outline(self.x, self.y, self.w, self.h, color=arcade.color.BLACK)

    def draw2(self):
        shifted_x = self.x - (self.w - self.fill * self.w) / 2
        arcade.draw_rectangle_filled(shifted_x, self.y, self.w * self.fill, self.h, color=arcade.color.ORANGE_PEEL)
        arcade.draw_rectangle_outline(self.x, self.y, self.w, self.h, color=arcade.color.BLACK)

