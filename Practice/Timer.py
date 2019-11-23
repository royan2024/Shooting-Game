import arcade

class Timer:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.time = 0

    def update(self, delta_time):
        self.time += delta_time

    def draw(self):
        min = self.time // 60
        if min < 10:
            min = "0%d" % min

        sec = int(self.time % 60)
        if sec < 10:
            sec = "0%d" % (sec)

        text = "Time: " + str(min) + ":" + str(sec)
        arcade.draw_text(text, self.x, self.y, arcade.color.BLACK, 20)