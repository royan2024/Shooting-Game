import arcade
from Constants import *

class Square:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

        self.velocity_x = 0
        self.velocity_y = 0
        self.acceleration_x = 0
        self.acceleration_y = 0
        self.max_speed = 20

        self.visible = True

    def update_velocity(self):
        if self.acceleration_x == 0 and self.velocity_x != 0:
            self.velocity_x = max(0, abs(self.velocity_x) - 0.5) * (self.velocity_x / abs(self.velocity_x))
        else:
            if self.velocity_x * self.acceleration_x < 0:
                multiplier = 2
            else:
                multiplier = 1
            self.velocity_x = max(-self.max_speed, min(self.max_speed, self.velocity_x + self.acceleration_x * multiplier))

        if self.acceleration_y == 0 and self.velocity_y != 0:
            self.velocity_y = max(0, abs(self.velocity_y) - 0.5) * (self.velocity_y / abs(self.velocity_y))
        else:
            if self.velocity_y * self.acceleration_y < 0:
                multiplier = 2
            else:
                multiplier = 1
            self.velocity_y = max(-self.max_speed, min(self.max_speed, self.velocity_y + self.acceleration_y))

    def draw(self):
        if self.visible:
           arcade.draw_rectangle_filled(self.x, self.y, self.size, self.size, self.color)

    def update(self):
        self.update_velocity()

        self.x += self.velocity_x
        self.y += self.velocity_y

        if self.x < self.size / 2:
            self.x = self.size / 2
            self.velocity_x = -self.velocity_x
        if self.x > SCREEN_WIDTH - self.size / 2:
            self.x = SCREEN_WIDTH - self.size / 2
            self.velocity_x = -self.velocity_x

        if self.y < self.size / 2:
            self.y = self.size / 2
            self.velocity_y = -self.velocity_y
        if self.y > SCREEN_HEIGHT - self.size / 2:
            self.y = SCREEN_HEIGHT - self.size / 2
            self.velocity_y = -self.velocity_y
