import arcade

class Character:
    def __init__(self, x, y, attack_speed):
        self.x = x
        self.y = y
        self.attack_speed = attack_speed
        #self.sprite = arcade.Sprite("resources/yumdda.png", float(1/66))


    def draw(self):
        #self.sprite.draw()
        arcade.draw_rectangle_filled(self.x, self.y, 20, 20, arcade.color.BLUE)

    def update(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y
