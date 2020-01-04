from arcade.key import *
from arcade import MOUSE_BUTTON_LEFT


BEHAVIOR = {
   "left": [A, LEFT],
   "right": [D, RIGHT],
   "up": [W, UP],
   "down": [S, DOWN],
   "shoot": [MOUSE_BUTTON_LEFT, SPACE],
   "select": [MOUSE_BUTTON_LEFT],
   "r": [R],
   "q": [Q]
}

def check_pressed(key, pressed):
   if key not in BEHAVIOR:
       return False
   return len(set(BEHAVIOR[key]) & set(pressed)) > 0

