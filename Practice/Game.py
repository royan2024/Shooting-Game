import arcade
from Constants import *
from arcade.key import *
from Square import Square
from Timer import Timer
import random

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.started = False
        self.cleared = False
        self.score = 0

        self.timer = Timer(10, height - 30)
        self.square = Square(width // 2, height // 2, CHAR_SIZE, arcade.color.YELLOW)
        self.special_objective = Square(random.randint(0, 800), random.randint(0, 600), 4, arcade.color.RED)
        self.objectives = []
        for i in range(OBJ_COUNT):
            x = random.randint(OBJ_SIZE // 2, width - OBJ_SIZE // 2)
            y = random.randint(OBJ_SIZE // 2, height - OBJ_SIZE // 2)
            self.objectives.append(Square(x, y, OBJ_SIZE, arcade.color.WHITE))

            #self.special_objective
            #색은 arcade.color.red
            #size 4
            #self.special_objective.max_speed = 40


    def on_key_press(self, symbol: int, modifiers: int):
        if self.cleared:
            return

        self.started = True
        if symbol == arcade.key.LEFT:
            self.square.acceleration_x = -1
        if symbol == arcade.key.RIGHT:
            self.square.acceleration_x = 1
        if symbol == arcade.key.UP:
            self.square.acceleration_y = 1
        if symbol == arcade.key.DOWN:
            self.square.acceleration_y = -1


    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == LEFT or symbol == RIGHT:
            self.square.acceleration_x = 0
        if symbol == UP or symbol == DOWN:
            self.square.acceleration_y = 0

    def on_update(self, delta_time: float):
        if not self.started or self.cleared:
            return
        self.timer.update(delta_time)
        self.square.update()
        self.update_objects()
        self.collide()

        if self.score == len(self.objectives):
            self.cleared = True

    def on_draw(self):
        arcade.start_render()
        self.timer.draw()
        for obj in self.objectives:
            obj.draw()
        self.square.draw()
        self.special_objective.draw()


        if self.cleared or not self.special_objective.visible:
            self.clear()
            arcade.draw_text("FINISHED", self.width // 2, self.height // 2, arcade.color.BLACK, 50, anchor_x="center")

    def update_objects(self):

        curr_acc_x = self.special_objective.acceleration_x
        curr_acc_y = self.special_objective.acceleration_y
        new_acc_x = random.random() * 4 - 2
        new_acc_y = random.random() * 4 - 2
        if abs(curr_acc_x - new_acc_x) > 1 and curr_acc_x != 0:
            self.special_objective.acceleration_x = curr_acc_x - (curr_acc_x / abs(curr_acc_x))
        else:
            self.special_objective.acceleration_x = new_acc_x

        if abs(curr_acc_y - new_acc_y) > 1 and curr_acc_y != 0:
            self.special_objective.acceleration_y = curr_acc_y - (curr_acc_y / abs(curr_acc_y))
        else:
            self.special_objective.acceleration_y = new_acc_y
        self.special_objective.update()


        for obj in self.objectives:
            curr_acc_x = obj.acceleration_x
            curr_acc_y = obj.acceleration_y
            new_acc_x = (random.random() - 0.5) * 2
            new_acc_y = (random.random() - 0.5) * 2
            if abs(curr_acc_x - new_acc_x) > 0.3 and curr_acc_x != 0:
                obj.acceleration_x = curr_acc_x - (curr_acc_x / abs(curr_acc_x)) * 0.3
            else:
                obj.acceleration_x = new_acc_x

            if abs(curr_acc_y - new_acc_y) > 0.3 and curr_acc_y != 0:
                obj.acceleration_y = curr_acc_y - (curr_acc_y / abs(curr_acc_y)) * 0.3
            else:
                obj.acceleration_y = new_acc_y
            obj.update()

            #special object를 업데이트
            #기존 acceleation on 1~-1 근데 2~-2 로 바꾸자


    def collide(self):
        if abs(self.square.x - self.special_objective.x) < (CHAR_SIZE + OBJ_SIZE) / 2 \
                and abs(self.square.y - self.special_objective.y) < (CHAR_SIZE + OBJ_SIZE) / 2 \
                and self.special_objective.visible:
            self.special_objective.visible = False

        for obj in self.objectives:
            if abs(self.square.x - obj.x) < (CHAR_SIZE + OBJ_SIZE) / 2 \
                    and abs(self.square.y - obj.y) < (CHAR_SIZE + OBJ_SIZE) / 2 \
                    and obj.visible:
                obj.visible = False
                self.score += 1
                #collision 처리도 해주는데, special object를 건드리는 순간 self.cleared를 바꿔주자

if __name__ == "__main__":
    Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_background_color(arcade.color.ICEBERG)
    arcade.run()