import arcade
import Bullet
import random
from Character import *


class Enemy:
    def __init__(self, x, y, hp=5, size=10, attack_speed=0.3):
        self.x = x
        self.y = y
        self.size = size
        self.attack_speed = attack_speed
        self.hp = hp
        self.visible = True
        self.acc = (random.randint(-6000, 6000), random.randint(-6000, 6000))
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

    def update(self, delta_time):
        self.x += 0.5 * self.acc[0] * delta_time**2
        self.y += 0.5 * self.acc[1] * delta_time**2
        if self.x > SCREEN_WIDTH:
            self.x = SCREEN_WIDTH
            self.acc = (self.acc[0] * -1, self.acc[1])

        if self.x < 0:
            self.x = 0
            self.acc = (self.acc[0] * -1, self.acc[1])

        if self.y > SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT
            self.acc = (self.acc[0], self.acc[1] * -1)
        if self.y < 0:
            self.y = 0
            self.acc = (self.acc[0], self.acc[1] * -1)
        self.sprite.position = (self.x, self.y)

#accelration 뒤집기

