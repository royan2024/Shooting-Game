import random
from Enemy import Enemy
from Character import Character
from Timer import Timer
from ScoreCalculator import ScoreCalculator
import Bullet
from Constants import *
from Configure import *
import arcade
from Scene.BaseScene import BaseScene
from Scene.StartScene import StartScene

class MainScene(BaseScene):
    def __init__(self):
        super().__init__()
        self.scene = StartScene
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
        self.timer = Timer(10, SCREEN_HEIGHT - 30)
        self.time = 0
        self.score = ScoreCalculator()
        self.total_score = 0
        self.finished = False

    def draw(self):
        for bullet in self.enemy_bullets:
            bullet.draw()
        for enemy in self.enemies:
            enemy.draw()
        self.character.draw()
        for bullet in self.bullets:
            bullet.draw()
        self.timer.draw()

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
            self.scene.draw()
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

