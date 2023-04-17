import pygame,sys,pathy,random
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
rndm = [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
#random.seed(2)
#random.seed(1545455545554)
random.seed("gfsjdgfhjghjjs")
"""matrix = [
  [1, 1, 1, 1, 1, 1, 0, 1],
  [1, 0, 1, 1, 1, 1, 1, 1],
  [1, 0, 0, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1],
  [0, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 1, 1]
]"""
wh = 24
matrix = [
    [random.choice(rndm) for i in range(wh)] for r in range(wh)
]

p = pathy.matrix(matrix)
grid = Grid(matrix=p.gen())


start = grid.node(0, 0)
end = grid.node(4, 5)

#finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
#path, runs = finder.find_path(start, end, grid)
#print(path)
#print('operations:', runs, 'path length:', len(path))
#print(grid.grid_str(path=path, start=start, end=end))

pthr = pathy.pathRUN()
pthRZ = pathy.pathRQ(grid,(15, 0),p.most)
pthr.queue.put(pthRZ)
pthRz = pathy.pathRQ(grid,(0,0),p.most)
pthr.queue.put(pthRz)

pygame.init()
scr = pygame.display.set_mode((500,500))

font = pygame.font.Font(None, 12)
clock = pygame.time.Clock()
while True:
    clock.tick(30)
    scr.fill((0,0,0))
    scr.blit(font.render(str(clock.get_fps()),True,(255,255,255)),(10,485))


    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x]:
                scr.fill(p.calc(x,y),(x*20,y*20,20,20))
            scr.blit(font.render(str(p.mtrxdz[y][x]),True,(255,255,255),(0,0,0)),((x*20)+1,(y*20)+1))

    if pthRz.st == pathy.rqState.done:
        prv = pthRz.St
        for i in pthRz.pth: 
            i = ((i[0]*20)+10,(i[1]*20)+10)
            pygame.draw.line(scr,(255,0,0),prv,i)
            prv = i

    if pthRZ.st == pathy.rqState.done:
        prv = pthRZ.St
        for i in pthRZ.pth: 
            i = ((i[0]*20)+10,(i[1]*20)+10)
            pygame.draw.line(scr,(255,255,0),prv,i)
            prv = i

    pygame.display.flip()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()