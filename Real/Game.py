#bullet 이랑 enemy 랑 닿으면 사라진다
#사라지는 처리는 enemy visible 을 끄면 됨, bullet 도 visible 을 끄면 됨
#visible 하지안은 enemy 와 bullet 은 충돌하지 않음
#다없어지면 victory

import arcade
import random
import Bullet
import Enemy
from Constants import *
from Character import Character
from Configure import *
from Enemy import Enemy

class Game(arcade.Window):
   def __init__(self):
       super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Shooting Game")
       self.enemies = []
       for i in range(5):
           x = random.randint(20, 780)
           y = random.randint(320, 580)
           enemy = Enemy(x, y)
           self.enemies.append(enemy)

       self.character = Character(400, 50)
       self.pressed = []
       self.mouse_position = (0, 0)

       self.bullets = []
       self.recent_fire = 0
       self.enemy_bullets = []
       self.recent_enemy_fire = 0
       self.time = 0
       self.finished = False

   def on_draw(self):
       arcade.start_render()
       for bullet in self.enemy_bullets:
           bullet.draw()
       for enemy in self.enemies:
           enemy.draw()
       self.character.draw()
       for bullet in self.bullets:
           bullet.draw()


   def on_update(self, delta_time: float):
       delta_x = 0
       delta_y = 0
       if not self.finished:
           if check_pressed("left", self.pressed):
               delta_x -= 5
           if check_pressed("right", self.pressed):
               delta_x += 5
           if check_pressed("up", self.pressed):
               delta_y += 5
           if check_pressed("down", self.pressed):
               delta_y -= 5
           self.character.update(delta_x, delta_y)

       for bullet in self.bullets:
           bullet.update(delta_time)

       for bullet in self.enemy_bullets:
           bullet.update(delta_time)

       if not self.finished:
           for enemy in self.enemies:
               enemy.update(delta_time)

       self.time += delta_time
       if check_pressed("shoot", self.pressed) and not self.finished:
           if self.recent_fire == 0 or self.recent_fire + self.character.attack_speed < self.time:
               x = self.character.x
               y = self.character.y + 15
               bullet = Bullet.create_normal_bullet(x, y, (self.mouse_position[0] - x, self.mouse_position[1] - y))
               self.bullets.append(bullet)
               self.recent_fire = self.time

       #지금은 적 fire가 임시구현이라 하드코딩
       if not self.finished:
           if self.recent_enemy_fire + 1 < self.time:
               self.recent_enemy_fire = self.time
               for enemy in self.enemies:
                   if enemy.visible:
                       self.enemy_bullets.extend(enemy.fire())

       self.on_collide()

       delete_list = []
       for i, bullet in enumerate(self.bullets):
           if bullet.y > 600:
               delete_list.insert(0, i)
       for i in delete_list:
           bullet = self.bullets[i]
           self.bullets.pop(i)
           del bullet

       delete_list = []
       for i, bullet in enumerate(self.enemy_bullets):
           if bullet.x > 800 or bullet.x < 0 or\
                   bullet.y > 600 or bullet.y < 0:
               delete_list.insert(0, i)
       for i in delete_list:
           bullet = self.enemy_bullets[i]
           self.enemy_bullets.pop(i)
           del bullet

   def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
       self.mouse_position = (x, y)

   def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
       self.pressed.append(button)

   def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
       self.pressed.remove(button)

   def on_key_press(self, symbol: int, modifiers: int):
       self.pressed.append(symbol)

   def on_key_release(self, symbol: int, modifiers: int):
       self.pressed.remove(symbol)

   def on_collide(self):
       for enemy in self.enemies:
           for bullet in self.bullets:
               if abs(bullet.x - enemy.x) < bullet.size + enemy.size / 2 \
                       and abs(bullet.y - enemy.y) < bullet.size + enemy.size / 2 \
                       and enemy.visible\
                       and bullet.visible:
                   enemy.hp -= 1
                   if enemy.hp == 0:
                       enemy.visible = False
                   bullet.visible = False

       for ebullet in self.enemy_bullets:
           if abs(ebullet.x - self.character.x) < ebullet.size + self.character.size / 2 \
                       and abs(ebullet.y - self.character.y) < ebullet.size + self.character.size / 2:
               ebullet.visible = False
               self.character.visible = False
               self.finished = True





if __name__ == "__main__":
   Game()
   arcade.set_background_color(arcade.color.WHITE)
   arcade.run()

