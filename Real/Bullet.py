import arcade
import Constants

class _Bullet:
    def __init__(self, x, y, direction, size, speed, is_enemy):
        self.x = x
        self.y = y
        self.direction = direction
        self.size = size
        self.speed = speed
        self.is_enemy = is_enemy
        self.visible = True
        if is_enemy:
            self.sprite = arcade.Sprite("resources/bentley.png", float(1/24))
        else:
            self.sprite = arcade.Sprite("resources/hood.png", float(1/16))

    #    if is_enemy:
     #       self.sprite = arcade.Sprite("resources/0.png", float(1/20))
      #  else:
       #     self.sprite = arcade.Sprite("resources/circle.png", float(1/66))

        self.sprite.position = (self.x, self.y)

    def draw(self):
        if self.visible:
            self.sprite.draw()

    def update(self, delta_time):
        delta_x = self.speed * self.direction[0] * delta_time
        delta_y = self.speed * self.direction[1] * delta_time
        self.x += delta_x
        self.y += delta_y
        self.sprite.position = (self.x, self.y)



#FACTORY PATTERN
#정해진 규칙에 따라 Instance를 생성
#득징: 항상 Instance를 리턴하는 Method거나 Class의 Method
def create_normal_bullet(x, y, direction: tuple, is_enemy=False):
    return _Bullet(x, y, _normalize(direction), Constants.BULLET_SIZE, Constants.BULLET_SPEED, is_enemy)

def create_fast_bullet(x, y, direction: tuple, is_enemy=False):
    return _Bullet(x, y, _normalize(direction), Constants.BULLET_SIZE, Constants.BULLET_SPEED * 3, is_enemy)

def _normalize(direction):
    x = direction[0]
    y = direction[1]
    length = pow(x**2 + y**2, 1/2)
    return x / length, y / length