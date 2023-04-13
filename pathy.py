import numpy as np
import pygame,threading,queue,enum
import time
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

class rqState(enum.Enum):
    waiting = 0
    in_progress = 1
    done = 2
    FAILED = 3

class pathState(enum.Enum):
    no_path = 0
    gen = 1
    run = 2

mx = pygame.Color(0,255,0)
mn = pygame.Color(0,0,255)


class pathRQ:
    def __init__(self,grid:Grid,s,e) -> None:
        self.st = rqState.waiting
        self.g  = grid
        self.g.cleanup()
        self.s,self.e = grid.node(*s),grid.node(*e)
        self.S = s
        self.St = ((s[0]*20)+10,(s[1]*20)+10)
        self.pth = None

class pathRUN:
    def __init__(self) -> None:
        self.thrd =threading.Thread(None,self.run,daemon=True)
        self.queue = queue.Queue()
        self.thrd.start()
    def run(self):
        while True:
            r:pathRQ = self.queue.get()
            r.g.cleanup()
            r.st = rqState.in_progress
            finder = AStarFinder(diagonal_movement=DiagonalMovement.only_when_no_obstacle)
            path, runs = finder.find_path(r.s, r.e, r.g)
            print('operations:', runs, 'path length:', len(path))
            print(r.g.grid_str(path=path, start=r.s, end=r.e))
            r.pth = path
            if len(path) == 0: 
                r.st = rqState.FAILED
            else:
                r.st = rqState.done
            time.sleep(1)


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
                if self.mtrxdz[r][i] > 0:
                    V = ((self.mv)-(self.mtrxdz[r][i]+0.1))*10
                    if V <= 0:
                        V = 1
                    R.append(V)
                else:
                    R.append(0)
            g.append(R)
        return g




    def dist(self):
        #print(self.mtrx)
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
                                    #print(d)
                                else: 
                                  #print(d)
                                  pass
                else:
                    #print(self.mtrx[Y][X])
                    dzt = 0.0
                if dzt > most:
                    most = dzt
                    mpos = (X,Y)
                R.append(round(dzt*10)/10)
            self.mtrxdz.append(R)
        self.most = mpos
        self.mv = most


class pathingGroup(pygame.sprite.AbstractGroup):
    def update(self, runer:pathRUN,mtrx:matrix,grid:Grid):
        """call the update method of every member sprite

        Group.update(*args, **kwargs): return None

        Calls the update method of every member sprite. All arguments that
        were passed to this method are passed to the Sprite update function.

        """
        for sprite in self.sprites():
            sprite.path(runer,mtrx,grid)

class PathingSprite(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, img):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = img
       self.pst = pathState.no_path
       self.paths = None

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect:pygame.Rect = self.image.get_rect()
    def path(self, runer:pathRUN,mtrx:matrix,grid:Grid) -> None:
        if self.pst == pathState.no_path:
            self.paths = pathRQ(grid,self.rect.center,mtrx.most)
            runer.queue.put(self.paths)
            self.pst = pathState.gen


