from Position import Position

class Cell:

    def __init__(self, position: Position = None, _type = "Cell"):
        self.position = position
        self.type = _type

    def __str__(self):
        return "{ " + "position: {}".format(str(self.position)) + ", type: {}".format(self.type) + " }"


