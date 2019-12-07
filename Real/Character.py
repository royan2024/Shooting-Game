import arcade

class Character:
    def __init__(self, x, y, size=20, attack_speed=0.3):
        self.x = x
        self.y = y
        self.size = size
        self.attack_speed = attack_speed
        self.visible = True
        self.sprite = arcade.Sprite("resources/yumdda.png", float(1/66))


    def draw(self):
        if self.visible:
            self.sprite.draw()
            #arcade.draw_rectangle_filled(self.x, self.y, self.size, self.size, arcade.color.BLUE)

    def update(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y
