from Scene.BaseScene import BaseScene
import os

class LeaderBoardScene(BaseScene):
    def __init__(self, recent_score=None):
        super().__init__()

        path = "Data/LeaderBoard.txt"
        if os.path.exists(path):
            f = open(path, "w")
            f.close()

        self.scores = []
        with open(path, "r") as f:
            lines = f.readlines()
            for line in lines:
                data = line.split()
                self.scores.append([int(data[1]), data[0]])

    def binary_search(self, recent_score):
        start = 0
        end = len(self.scores) - 1
        while start <= end:
            center = (start + end) // 2
            if recent_score > self.scores[center][0]:
                start = center + 1
            elif recent_score < center:
                end = center - 1
            elif recent_score == center:
                return center
        destination = start
        return destination





if __name__ == "__main__":
    os.chdir("..")
    scores = []
    with open("Data/Sample.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            data = line.split()
            scores.append([int(data[1]), data[0]])
    scores.sort(reverse=True)
    print(scores)