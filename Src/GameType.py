from enum import Enum

class GameType(Enum):
    QUIT = -1
    PLAYER_VS_PLAYER = 0
    PLAYER_VS_AI = 1
    AI_VS_AI = 2