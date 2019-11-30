import arcade

class Bullet:
    def __init__(self, x, y, size, speed):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.visible = True

    def draw(self):
        if self.visible:
            arcade.draw_circle_filled(self.x, self.y, self.size, arcade.color.ORANGE)

    def update(self, delta_time):
        self.y += self.speed * delta_time
