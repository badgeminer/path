import numpy as np
import pygame
class matrix:
    def __init__(self,mtrx) -> None:
        self.mtrx = mtrx
        self.mtrxdz = []
        self.dist()

    def dist(self):
        print(self.mtrx)
        for X in range(len(self.mtrx)):
            R = []
            for Y in range(len(self.mtrx[X])):
                if self.mtrx[X][Y] >= 1:
                    dzt = 100.0
                    for x in range(len(self.mtrx)):
                        for y in range(len(self.mtrx[x])):
                            if (self.mtrx[x][y] >= 1): 
                              pass
                            else:
                                d = pygame.math.Vector2(X, Y).distance_to((x,y))
                                if d <= dzt:
                                    dzt = d
                                    print(d)
                                else: 
                                  print(d)
                else:
                    print(self.mtrx[X][Y])
                    dzt = 0.0
                R.append(round(dzt*10)/10)
            self.mtrxdz.append(R)
