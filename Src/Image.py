from enum import Enum


class Image(Enum):
    SQUARE = ["../Image/carre.png", (170, 170)]
    PAWN_BLACK = ["../Image/pawnblack.png", (75, 75)]
    PAWN_WHITE = ["../Image/pawnwhite.png", (75, 75)]
    SELECTOR_SQUARE_ACTIVE = ["../Image/selecteuractif.png", (170, 170)]
    SELECTOR_SQUARE_PASSIVE = ["../Image/selecteur.png", (170, 170)]
    SELECTOR_PAWN_ACTIVE = ["../Image/selecteuractif.png", (75, 75)]
    SELECTOR_PAWN_PASSIVE = ["../Image/selecteur.png", (75, 75)]
    GRID = ["../Image/grille.png", (650, 650)]
    BACKGROUND = ["../Image/background.jpg", (1000, 800)]
