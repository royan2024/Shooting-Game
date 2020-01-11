from Scene.MainScene import MainScene
from Scene.StartScene import StartScene
import arcade

def to_main_scene():
    arcade.get_window().scene_transition(MainScene())

def to_start_scene():
    arcade.get_window().scene_transition(StartScene())

