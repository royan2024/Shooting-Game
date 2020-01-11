#q 눌르면 start scene
#review

from Scene.BaseScene import BaseScene
import Scene.SceneController as SceneController
from Constants import *
from Configure import *
import arcade

class StartScene(BaseScene):
    def __init__(self):
        super().__init__()
        self.button_width = 200
        self.button_height = 100
        self.button_position = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

        self.mouse_pressed = False
        self.pressed_inside = False
        self.released_inside = False

        self.button_pressed = False

    def draw(self):
        if self.button_pressed:
            arcade.draw_rectangle_filled(self.button_position[0], self.button_position[1],
                                         self.button_width, self.button_height,
                                         color=arcade.color.GRAY)
        else:
            arcade.draw_rectangle_filled(self.button_position[0], self.button_position[1],
                                         self.button_width, self.button_height,
                                         color=arcade.color.BLACK)

        arcade.draw_text("START GAME", self.button_position[0], self.button_position[1],
                     color=arcade.color.WHITE, font_size=20,
                     align="center", anchor_x="center", anchor_y="center")

    def update(self, delta_time):
        if check_pressed("select", self.pressed):
            if self.mouse_inside():
                #이제 막 눌림
                if not self.mouse_pressed:
                    self.pressed_inside = True
                    self.button_pressed = True
            else:
                #이제 막 눌림
                if not self.mouse_pressed:
                    self.pressed_inside = False

                self.button_pressed = False
        else:
            if self.mouse_inside():
                #이제 막 떼어짐
                if self.mouse_pressed and self.pressed_inside:
                    SceneController.to_main_scene()
            self.button_pressed = False

        self.mouse_pressed = len(set(BEHAVIOR["select"]) & set(self.pressed)) > 0

    def mouse_inside(self):
        return self.button_position[0] - self.button_width / 2 <= \
                    self.mouse_position[0] <= self.button_position[0] + self.button_width / 2 and \
                    self.button_position[1] - self.button_height / 2 <= \
                    self.mouse_position[1] <= self.button_position[1] + self.button_height / 2

