import arcade

class BaseScene:
    def __init__(self):
        self.mouse_position = (0, 0)
        self.pressed = []

    def draw(self):
        raise NotImplementedError

    def update(self, delta_time):
        raise NotImplementedError