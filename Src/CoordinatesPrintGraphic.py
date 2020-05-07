import enum
import numpy as np

class CoordinatesPrintGraphic(enum.Enum):
    STEP = 215
    #Position pawn init
    POSITION_PRINT_PAWN_INIT = np.any([ # Il faut utiliser 'any' au lieu de array sinon ça veut pas marcher
            [(750,50),(750,50+STEP),(750,50+2*STEP)], #Column 1 (and not line!)
            [(850,50),(850,50+STEP),(850,50+2*STEP)]]) #Column 2
    #Position pawn
    POSITION_PRINT_PAWN = np.any([
            [(25,25),(25+STEP,25),(25+2*STEP,25)], #Column 1 (and not line!)
            [(25,25+STEP),(25+STEP,25+STEP),(25+2*STEP,25+STEP)], #Column 2
            [(25,25+2*STEP),(25+STEP,25+2*STEP),(25+2*STEP,25+2*STEP)]]) #Column 3
    #Position square
    POSITION_PRINT_SQUARE = np.any([
            [(25,25),(25+STEP,25),(25+2*STEP,25)], #Column 1 (and not line!)
            [(25,25+STEP),(25+STEP,25+STEP),(25+2*STEP,25+STEP)], #Column 2
            [(25,25+2*STEP),(25+STEP,25+2*STEP),(25+2*STEP,25+2*STEP)]]) #Column 3
