from Scene.BaseScene import BaseScene
import os
import arcade

class LeaderBoardScene(BaseScene):
    def __init__(self, player_name=None, recent_score=None):
        super().__init__()
        self.leader_board = LeaderBoard(player_name, recent_score).scores
        self.new_data = [recent_score, player_name]

    def draw(self):
        arcade.start_render()
        x = 400
        y = 500
        for i in range(min(10, len(self.leader_board))):
            name = self.leader_board[i][1]
            if self.new_data == self.leader_board[i]:
                color = arcade.color.RED
                name = "new!   " + name
            else:
                color = arcade.color.BLACK
            #이름
            arcade.draw_text(name,
                             x - 10, y, color,
                             font_size=24,
                             align="right", anchor_x="right", anchor_y="top")
            #점수
            arcade.draw_text(str(self.leader_board[i][0]),
                             x + 10, y, color,
                             font_size=24, anchor_y="top")
            y -= 40

    def update(self, delta_time):
        return

class LeaderBoard:
    def __init__(self, player_name=None, recent_score=None):
        path = "Data/LeaderBoard.txt"
        if not os.path.exists(path):
            f = open(path, "w")
            f.close()

        self.scores = []
        with open(path, "r") as f:
            lines = f.readlines()
            for line in lines:
                data = line.split()
                self.scores.append([int(data[1]), data[0]])

        if recent_score is not None and player_name is not None:
            self.scores.insert(self.binary_search(recent_score), [recent_score, player_name])

            with open(path, "w") as f:
                for s in self.scores[:10]:
                    f.write(s[1] + " " + str(s[0]) + "\n")

    def binary_search(self, recent_score):
        start = 0
        end = len(self.scores) - 1
        while start <= end:
            center = (start + end) // 2
            if recent_score < self.scores[center][0]:
                start = center + 1
            elif recent_score > self.scores[center][0]:
                end = center - 1
            else:
                return center + 1
        destination = start
        return destination





if __name__ == "__main__":
    os.chdir("..")
