from Scene.MainScene import MainScene
from Scene.StartScene import StartScene
from Scene.LeaderBoardScene import LeaderBoardScene
import arcade

def to_main_scene():
    arcade.get_window().scene_transition(MainScene())

def to_start_scene():
    arcade.get_window().scene_transition(StartScene())

def to_leaderboard_scene(player_name = None, recent_score=None):
    arcade.get_window().scene_transition(LeaderBoardScene(player_name, recent_score))