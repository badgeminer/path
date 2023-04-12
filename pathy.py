import numpy as np
import pygame,threading,queue,enum
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

class rqState(enum.Enum):
    waiting = 0
    in_progress = 1
    done = 2

mx = pygame.Color(0,255,0)
mn = pygame.Color(0,0,255)

class pathRQ:
    def __init__(self,grid:Grid,s,e) -> None:
        self.st = rqState.waiting
        self.g  = grid
        self.g.cleanup()
        self.s,self.e = s,e
        self.pth = None

class pathRUN:
    def __init__(self) -> None:
        self.thrd =threading.Thread(None,self.run,daemon=True)
        self.queue = queue.Queue()
        self.thrd.start()
    def run(self):
        while True:
            r:pathRQ = self.queue.get()
            r.st = rqState.in_progress
            finder = AStarFinder(diagonal_movement=DiagonalMovement.only_when_no_obstacle)
            path, runs = finder.find_path(r.s, r.e, r.g)
            print('operations:', runs, 'path length:', len(path))
            print(r.g.grid_str(path=path, start=r.s, end=r.e))
            r.pth = path
            r.st = rqState.done


class matrix:
    def __init__(self,mtrx) -> None:
        self.mtrx = mtrx
        self.mtrxdz = []
        self.most = (0,0)
        self.mv = 0

        self.dist()
        self.calcd = {}
    def calc(self,x,y):
        if (x,y) in self.calcd:
            return self.calcd[(x,y)]
        d = self.mtrxdz[y][x]
        dc = (d/self.mv)
        if dc > 1: dc = 1
        try:
            C = mn.lerp(mx,dc)
        except:
            C = mn
        self.calcd[(x,y)] = C
        return C
    def gen(self):
        g = []
        for r in range(len(self.mtrx)):
            R = []
            for i in range(len(self.mtrx[r])):
                R.append(self.mtrxdz[r][i])
            g.append(R)
        return g




    def dist(self):
        print(self.mtrx)
        most = 0
        mpos = (-1,-1)
        for Y in range(len(self.mtrx)):
            R = []
            for X in range(len(self.mtrx[Y])):
                if self.mtrx[Y][X] >= 1:
                    dzt = 100.0
                    for y in range(len(self.mtrx)):
                        for x in range(len(self.mtrx[y])):
                            if (self.mtrx[y][x] >= 1): 
                              pass
                            else:
                                d = pygame.math.Vector2(X, Y).distance_to((x,y))
                                if d <= dzt:
                                    dzt = d
                                    print(d)
                                else: 
                                  print(d)
                else:
                    print(self.mtrx[Y][X])
                    dzt = 0.0
                if dzt > most:
                    most = dzt
                    mpos = (X,Y)
                R.append(round(dzt*10)/10)
            self.mtrxdz.append(R)
        self.most = mpos
        self.mv = most
