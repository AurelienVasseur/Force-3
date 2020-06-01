from Player import Player
from Color import Color
from GameBoard import GameBoard
import sys

class ArtificialIntelligence(Player):

    def __init__(self, color: Color, isTurnActive = False, selector = None, deepness = 4):
        super(ArtificialIntelligence, self).__init__(color, isTurnActive, selector)
        self.deepness = deepness


    def minimax(self, gameBoard, depth, alpha, beta, players):
        # BLACK MAXIMIZES
        # WHITE MINIMIZES
        if(depth == 0 or gameBoard.isGameEnded()):
            return gameBoard.getPlayerScore(self.activePlayer(players))
        
        maximizingPlayer = self.activePlayer(players).color == Color.BLACK
        infinity = sys.maxsize

        possibleMoves = gameBoard.getPossibleMoves(self.activePlayer(players))

        if(maximizingPlayer):
            # maximizing
            maxEval = -infinity
            for possibleMove in possibleMoves:
                evaluation = self.minimax(self.simulateMove(gameBoard, possibleMove), depth - 1, alpha, beta, self.switchActivePlayer(players))
                maxEval = max(maxEval, evaluation)
                alpha = max(alpha, evaluation)
                if (beta <= alpha):
                    break
            return maxEval
        else:
            # minimizing
            minEval = infinity
            for possibleMove in possibleMoves:
                evaluation = self.minimax(self.simulateMove(gameBoard, possibleMove), depth - 1, alpha, beta, self.switchActivePlayer(players))
                minEval = min(minEval, evaluation)
                beta = min(beta, evaluation)
                if (beta <= alpha):
                    break
            return minEval
    

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
        return newGameBoard


    
    def playBestMove(self, gameBoard, players):
        infinity = sys.maxsize
        alpha = -infinity
        beta = infinity
        if(self.activePlayer(players).color != self.color):
            players = self.switchActivePlayer(players)
        
        values = []
        possibleMoves = gameBoard.getPossibleMoves(self.activePlayer(players))
        for possibleMove in possibleMoves:
            values.append(self.minimax(self.simulateMove(gameBoard, possibleMove), self.deepness, alpha, beta, players))
            
            
        if(self.color == Color.BLACK):
            # search max value
            bestMoveIndex = -1
            maxValue = -infinity
            for i in range(len(values)):
                if(values[i] > maxValue):
                    maxValue = values[i]
                    bestMoveIndex = i
            gameBoard.move(possibleMoves[bestMoveIndex])
        else:
            # search min value
            bestMoveIndex = -1
            minValue = infinity
            for i in range(len(values)):
                if(values[i] < minValue):
                    minValue = values[i]
                    bestMoveIndex = i
            gameBoard.move(possibleMoves[bestMoveIndex])

