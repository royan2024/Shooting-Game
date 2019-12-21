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

        msec = int((self.time * 100) % 100)
        if msec < 10:
            msec = "0%d" % msec

        text = "Time: " + str(min) + ":" + str(sec) + "." + str(msec)
        arcade.draw_text(text, self.x, self.y, arcade.color.BLACK, 20)