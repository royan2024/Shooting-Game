import arcade
from Constants import *


class Character:
   def __init__(self, x, y, size=20, attack_speed=0.3):
       self.x = x
       self.y = y
       self.size = size
       self.attack_speed = attack_speed
       self.power_attack_speed = POWER_ATTACK_SPEED
       self.visible = True
       self.sprite = arcade.Sprite("resources/yumdda.png", float(1/66))
       self.sprite.position = (self.x, self.y)
       self.shield_sprite = arcade.Sprite("Resources/shield.png", float(2/55))
       self.shield_sprite.position = (self.x, self.y)
       self.is_shield_on = False


   def draw(self):
       if self.visible:
           self.sprite.draw()
           #arcade.draw_rectangle_filled(self.x, self.y, self.size, self.size, arcade.color.BLUE)
           if self.is_shield_on:
               self.shield_sprite.draw()

   def update(self, delta_x, delta_y):
       self.x += delta_x
       self.y += delta_y
       if self.x > SCREEN_WIDTH:
           self.x = SCREEN_WIDTH
       if self.x < 0:
           self.x = 0
       if self.y > SCREEN_HEIGHT:
           self.y = SCREEN_HEIGHT
       if self.y < 0:
           self.y = 0
       self.sprite.position = (self.x, self.y)
       self.shield_sprite.position = (self.x, self.y)


