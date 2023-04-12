import pygame,sys,pathy
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

matrix = [
  [1, 1, 1, 1],
  [1, 0, 1, 1],
  [1, 1, 1, 1]
]
p = pathy.matrix(matrix)
grid = Grid(matrix=matrix)


start = grid.node(0, 0)
end = grid.node(2, 2)

finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
path, runs = finder.find_path(start, end, grid)

print('operations:', runs, 'path length:', len(path))
print(grid.grid_str(path=path, start=start, end=end))

pygame.init()
scr = pygame.display.set_mode((500,500))

font = pygame.font.Font(None, 12)

while True:
    scr.fill((0,0,0))

    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y]:
                scr.fill((255,255,255),(x*20,y*20,20,20))
            scr.blit(font.render(str(p.mtrxdz[x][y]),True,(255,255,255),(0,0,0)),((x*20)+5,(y*20)+5))

    pygame.display.flip()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()