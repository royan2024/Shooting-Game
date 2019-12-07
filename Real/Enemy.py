import arcade
import Bullet


class Enemy:
    def __init__(self, x, y, size=10, attack_speed=0.3):
        self.x = x
        self.y = y
        self.size = size
        self.attack_speed = attack_speed
        self.visible = True
        self.sprite = arcade.Sprite("resources/tq.png", float(1/33))
        self.sprite.position = (self.x, self.y)

    def fire(self):
        bullets = []
        directions = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
        for i in range(8):
            bullets.append(Bullet.create_normal_bullet(self.x, self.y, directions[i], True))
        return bullets


    def draw(self):
        if self.visible:
            self.sprite.draw()
            #arcade.draw_rectangle_filled(self.x, self.y, self.size, self.size, arcade.color.RED)

    def update(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y
        self.sprite.position = (self.x, self.y)
