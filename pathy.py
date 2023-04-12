import numpy as np
import pygame
class matrix:
    def __init__(self,mtrx) -> None:
        self.mtrx = mtrx
        self.mtrxdz = []
        self.dist()

    def dist(self):
        for X in range(len(self.mtrx)):
            R = []
            for Y in range(len(self.mtrx[X])):
                if self.mtrx[X][Y]:
                    dzt = 100
                    for x in range(len(self.mtrx)):
                        for y in range(len(self.mtrx[x])):
                            if ((X == x) and (Y == y)) or (self.mtrx[X][Y] >= 1): 
                                pass
                            else:
                                d = pygame.math.Vector2(X, Y).distance_to((x,y))
                                if d < dzt:
                                    dzt = d
                else:
                    dzt = 0.0
                R.append(dzt)
            self.mtrxdz.append(R)
