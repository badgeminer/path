import unittest,pathy,random
from pathfinding.core.grid import Grid

rndm = [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

wh = 24
matrix = [
    [random.choice(rndm) for i in range(wh)] for r in range(wh)
]

p =pathy.matrix(matrix)

grid = Grid(matrix=p.gen())



class TesStringMethods(unittest.TestCase):
    def test_len(self):
        pthr = pathy.pathRUN()
        pthRZ = pathy.pathRQ(grid,(0, 0),p.most)
        pthr.queue.put(pthRZ)
        while pthRZ.st != pathy.rqState.done:
            pass
        self.assertTrue(len(pthRZ.pth)>0)
    #@unittest.skip("demonstrating skipping")
    def test_opp(self):
        pthr = pathy.pathRUN()
        pthRZ = pathy.pathRQ(grid,(1, 0),p.most)
        pthr.queue.put(pthRZ)
        while pthRZ.st != pathy.rqState.done:
            pass
        self.assertEquals(p.mtrxdz[pthRZ.pth[-1][0]][pthRZ.pth[-1][1]],p.mv)

if __name__ == '__main__':
    unittest.main()