import numpy as np

class CoordinatesPrintGraphic:
    def __init__(self):
        self.step = 215
        #Position pawn init
        self.positionsPrintPawnInit = np.array([
            [(750,50),(750,50+self.step),(750,50+2*self.step)], #Column 1 (and not line!)
            [(850,50),(850,50+self.step),(850,50+2*self.step)]]) #Column 2
        #Position pawn
        self.positionsPrintPawn = np.array([
            [(25,25),(25+self.step,25),(25+2*self.step,25)], #Column 1 (and not line!)
            [(25,25+self.step),(25+self.step,25+self.step),(25+2*self.step,25+self.step)], #Column 2
            [(25,25+2*self.step),(25+self.step,25+2*self.step),(25+2*self.step,25+2*self.step)]]) #Column 3
        #Position square
        self.positionsPrintSquare = np.array([
            [(25,25),(25+self.step,25),(25+2*self.step,25)], #Column 1 (and not line!)
            [(25,25+self.step),(25+self.step,25+self.step),(25+2*self.step,25+self.step)], #Column 2
            [(25,25+2*self.step),(25+self.step,25+2*self.step),(25+2*self.step,25+2*self.step)]]) #Column 3
