#bullet 이랑 enemy 랑 닿으면 사라진다
#사라지는 처리는 enemy visible 을 끄면 됨, bullet 도 visible 을 끄면 됨
#visible 하지안은 enemy 와 bullet 은 충돌하지 않음
#다없어지면 victory

import arcade
import random
from arcade.key import *
import Bullet
import Enemy
from Character import Character
from Enemy import Enemy

class Game(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, "Shooting Game")
        self.enemies = []
        for i in range(5):
            x = random.randint(20, 780)
            y = random.randint(320, 580)
            enemy = Enemy(x, y)
            self.enemies.append(enemy)

        self.character = Character(400, 50)
        self.pressed = {
            LEFT: False,
            RIGHT: False,
            UP: False,
            DOWN: False,
            SPACE: False
        }

        self.bullets = []
        self.recent_fire = 0
        self.enemy_bullets = []
        self.recent_enemy_fire = 0
        self.time = 0

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
        if self.pressed[LEFT]:
            delta_x -= 5
        if self.pressed[RIGHT]:
            delta_x += 5
        if self.pressed[UP]:
            delta_y += 5
        if self.pressed[DOWN]:
            delta_y -= 5
        self.character.update(delta_x, delta_y)

        for bullet in self.bullets:
            bullet.update(delta_time)

        for bullet in self.enemy_bullets:
            bullet.update(delta_time)

        self.time += delta_time
        if self.pressed[SPACE]:
            if self.recent_fire == 0 or self.recent_fire + self.character.attack_speed < self.time:
                x = self.character.x
                y = self.character.y + 15
                bullet = Bullet.create_normal_bullet(x, y, (0, 1))
                self.bullets.append(bullet)
                self.recent_fire = self.time

        #지금은 적 fire가 임시구현이라 하드코딩
        if self.recent_enemy_fire + 1 < self.time:
            self.recent_enemy_fire = self.time
            for enemy in self.enemies:
                if enemy.visible:
                    self.enemy_bullets.extend(enemy.fire())

        self.on_collide()

        delete_list = []
        for i, bullet in enumerate(self.bullets):
            if bullet.y > 600:
                delete_list.insert(i, 0)
        for i in delete_list:
            bullet = self.bullets[i]
            self.bullets.pop(i)
            del bullet


    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == LEFT:
            self.pressed[LEFT] = True
        if symbol == RIGHT:
            self.pressed[RIGHT] = True
        if symbol == UP:
            self.pressed[UP] = True
        if symbol == DOWN:
            self.pressed[DOWN] = True
        if symbol == SPACE:
            self.pressed[SPACE] = True

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == LEFT:
            self.pressed[LEFT] = False
        if symbol == RIGHT:
            self.pressed[RIGHT] = False
        if symbol == UP:
            self.pressed[UP] = False
        if symbol == DOWN:
            self.pressed[DOWN] = False
        if symbol == SPACE:
            self.pressed[SPACE] = False

    def on_collide(self):
        for enemy in self.enemies:
            for bullet in self.bullets:
                if abs(bullet.x - enemy.x) < bullet.size + enemy.size / 2 \
                        and abs(bullet.y - enemy.y) < bullet.size + enemy.size / 2 \
                        and enemy.visible\
                        and bullet.visible:
                    enemy.visible = False
                    bullet.visible = False

        for ebullet in self.enemy_bullets:
            if abs(ebullet.x - self.character.x) < ebullet.size + self.character.size / 2 \
                        and abs(ebullet.y - self.character.y) < ebullet.size + self.character.size / 2:
                ebullet.visible = False
                self.character.visible = False





if __name__ == "__main__":
    Game()
    arcade.set_background_color(arcade.color.WHITE)
    arcade.run()