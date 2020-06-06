from .StatusType import StatusType
from .WinType import WinType
from .Color import Color

class GameStatus():

    def __init__(self, status: StatusType, winType: WinType = None, winner: Color = None):
        self.status = status
        self.winType = winType
        self.winner = winner