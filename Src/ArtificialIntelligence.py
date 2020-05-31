from Player import Player
from Color import Color
from GameBoard import GameBoard

class ArtificialIntelligence(Player):

    def __init__(self, color: Color, isTurnActive = False, selector = None, deepness = 5):
        super(ArtificialIntelligence, self).__init__(color, isTurnActive, selector)
        self.deepness = deepness


    def minimax(self, gameBoard, depth, alpha, beta, players):
        # BLACK MAXIMIZES
        # WHITE MINIMIZES
        if(depth == 0 or gameBoard.isGameEnded()):
            return gameBoard.getPlayerScore(self.activePlayer(players))
        
        maximizingPlayer = self.activePlayer(players).color == Color.BLACK

        if(maximizingPlayer):
            # maximizing
            ...
        else:
            # minimizing
            ...
    

    def activePlayer(self, players):
        if(players[Color.BLACK.value].isTurnActive):
            return players[Color.BLACK.value]
        return players[Color.WHITE.value]

    def switchActivePlayer(self, players):
        updatedPlayers = []
        blackPlayer = players[Color.BLACK.value]
        updatedPlayers.append(Player(blackPlayer.color, blackPlayer.isTurnActive, blackPlayer.selector))
        whitePlayer = players[Color.WHITE.value]
        updatedPlayers.append(Player(whitePlayer.color, whitePlayer.isTurnActive, whitePlayer.selector))

        if(updatedPlayers[Color.BLACK.value].isTurnActive):
            updatedPlayers[Color.BLACK.value].isTurnActive = False
            updatedPlayers[Color.WHITE.value].isTurnActive = True
        else:
            updatedPlayers[Color.BLACK.value].isTurnActive = True
            updatedPlayers[Color.WHITE.value].isTurnActive = False
        
        return updatedPlayers


    def simulateMove(self, gameBoard, move):
        newGameBoard = GameBoard(gameBoard)
        newGameBoard.move(move)
        ...