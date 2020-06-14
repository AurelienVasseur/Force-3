

class Position:

    def __init__(self, x = -1, y = -1):
        self.x = x
        self.y = y

    def __str__(self):
        return "{ " + "x: {}".format(self.x) + ", y: {}".format(self.y) + " }"

