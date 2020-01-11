#mainscene = 새로운 gauge 추가 - self.power_gauge = Guage(..)
#self.character 에 attack_speed 공속 3 배 - constants 값을이용

#challenge
#power 버튼은 걍 쭉 게이지 감소
#다 찰때까지 못씀

#mainscene
#not is using power and gauge.fill = 0.1 그럼 is using power

#is_using_power가 켜지는 시점 - 최초로 power 버튼 누른때 and fill이 1.0

import random
from Components.Enemy import Enemy
from Components.Character import Character
from Components.Timer import Timer
from Components.Gauge import Gauge
from ScoreCalculator import ScoreCalculator
from Components import Bullet
from Constants import *
from Configure import *
import arcade
from Scene.BaseScene import BaseScene
import Scene.SceneController as SceneController

class MainScene(BaseScene):
    def __init__(self):
        super().__init__()
        self.enemies = []
        for i in range(ENEMY_COUNT):
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
        self.shield_gauge = Gauge(100, 40, 150, 25)
        self.power_gauge = Gauge(100, 80, 150, 25)
        self.timer = Timer(10, SCREEN_HEIGHT - 30)
        self.time = 0
        self.score = ScoreCalculator()
        self.total_score = 0
        self.finished = False
        self.is_using_shield = False
        self.is_using_power = False

    def draw(self):
        for bullet in self.enemy_bullets:
            bullet.draw()
        for enemy in self.enemies:
            enemy.draw()
        self.character.draw()
        for bullet in self.bullets:
            bullet.draw()
        self.timer.draw()
        self.shield_gauge.draw1()
        self.power_gauge.draw2()


        arcade.draw_text(
            "Score: %6d" % (self.score.calculate(self.timer.time, False)),
            SCREEN_WIDTH - 10,
            SCREEN_HEIGHT - 30,
            arcade.color.BLACK,
            font_size=20,
            align="right",
            anchor_x="right"
        )

        if self.finished:
            arcade.draw_text(
                str("Play Again?"),
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT - 400,
                arcade.color.BLACK,
                font_size=40,
                align="center",
                anchor_x="center"
            )
            arcade.draw_text(
                str(self.total_score),
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT - 200,
                arcade.color.BLACK,
                font_size=40,
                align="center",
                anchor_x="center"
            )

    def update(self, delta_time):
        delta_x = 0
        delta_y = 0
        if check_pressed("q", self.pressed):
            SceneController.to_start_scene()
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

            if check_pressed("shield", self.pressed):
                delta_shield = -delta_time * SHIELD_DECREASE
                self.shield_gauge.update(delta_shield)
                self.is_using_shield = self.shield_gauge.fill > 0
            else:
                delta_shield = delta_time * SHIELD_INCREASE
                self.shield_gauge.update(delta_shield)
                self.is_using_shield = False
            self.character.is_shield_on = self.is_using_shield

            if check_pressed("power", self.pressed):
                if not self.is_using_power:
                    if self.power_gauge.fill == 1:
                        self.is_using_power = True

            if self.is_using_power:
                delta_power = -delta_time * POWER_DECREASE
                self.power_gauge.update(delta_power)
                self.is_using_power = self.power_gauge.fill > 0
            else:
                delta_power = delta_time * POWER_INCREASE
                self.power_gauge.update(delta_power)
            self.character.is_power_on = self.is_using_power


        else:
            if check_pressed("r", self.pressed):
                self.reset()

        for bullet in self.bullets:
            bullet.update(delta_time)

        for bullet in self.enemy_bullets:
            bullet.update(delta_time)

        if not self.finished:
            for enemy in self.enemies:
                enemy.update(delta_time)

        if not self.finished:
            self.timer.update(delta_time)

        self.time += delta_time
        if self.is_using_power:
            if check_pressed("shoot", self.pressed) and not self.finished:
                if self.recent_fire == 0 or self.recent_fire + self.character.power_attack_speed < self.time:
                    x = self.character.x
                    y = self.character.y + 15
                    bullet = Bullet.create_normal_bullet(x, y, (self.mouse_position[0] - x, self.mouse_position[1] - y))
                    self.bullets.append(bullet)
                    self.recent_fire = self.time
        else:
            if check_pressed("shoot", self.pressed) and not self.finished:
                if self.recent_fire == 0 or self.recent_fire + self.character.attack_speed < self.time:
                    x = self.character.x
                    y = self.character.y + 15
                    bullet = Bullet.create_normal_bullet(x, y, (self.mouse_position[0] - x, self.mouse_position[1] - y))
                    self.bullets.append(bullet)
                    self.recent_fire = self.time

        # 지금은 적 fire가 임시구현이라 하드코딩
        if not self.finished:
            if self.recent_enemy_fire + 1 < self.time:
                self.recent_enemy_fire = self.time
                for enemy in self.enemies:
                    if enemy.visible:
                        self.enemy_bullets.extend(enemy.fire())

        self.on_collide()
        self.check_finish()

        delete_list = []
        for i, bullet in enumerate(self.bullets):
            if bullet.y > 600:
                delete_list.insert(0, i)
        for i in delete_list:
            bullet = self.bullets[i]
            self.bullets.pop(i)

        delete_list = []
        for i, bullet in enumerate(self.enemy_bullets):
            if bullet.x > 800 or bullet.x < 0 or \
                    bullet.y > 600 or bullet.y < 0:
                delete_list.insert(0, i)
        for i in delete_list:
            self.enemy_bullets.pop(i)

    def on_collide(self):
        for enemy in self.enemies:
            for bullet in self.bullets:
                if abs(bullet.x - enemy.x) < bullet.size + enemy.size / 2 \
                        and abs(bullet.y - enemy.y) < bullet.size + enemy.size / 2 \
                        and enemy.visible \
                        and bullet.visible:
                    enemy.hp -= 1
                    if not self.finished:
                        self.score.hit += 1
                    if enemy.hp == 0:
                        enemy.visible = False
                        if not self.finished:
                            self.score.kill += 1
                    bullet.visible = False

        for ebullet in self.enemy_bullets:
            if abs(ebullet.x - self.character.x) < ebullet.size + self.character.size / 2 \
                    and abs(ebullet.y - self.character.y) < ebullet.size + self.character.size / 2:
                ebullet.visible = False
                if not self.is_using_shield:
                    self.character.visible = False

    def check_finish(self):
        if self.finished:
            return
        is_win = True
        for enemy in self.enemies:
            is_win = is_win and not enemy.visible
        if is_win:
            self.finished = True
            self.total_score += self.score.calculate(self.timer.time, is_win)

        if not self.character.visible:
            self.finished = True
            self.total_score += self.score.calculate(self.timer.time, False)

    def reset(self):
        if self.finished:
            for enemy in self.enemies:
                if enemy.visible:
                    enemy.visible = False
            for bullet in self.bullets:
                if bullet.visible:
                    bullet.visible = False
            for ebullet in self.enemy_bullets:
                if ebullet.visible:
                    ebullet.visible = False
            if self.character.visible:
                self.character.visible = False

            self.__init__()

