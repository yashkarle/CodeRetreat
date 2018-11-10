import unittest

def num_neigh(grid, x, y):
    iterators = [-1,0,1]
    sum = 0
    for i in iterators:
        for j in iterators:
            if 0<x+i<len(grid) and 0<y+j<len(grid):
                sum = sum + grid[y+j][x+i]
    return sum - grid[y][x]

def should_die(grid, x,y):
    return True

class TestStringMethods(unittest.TestCase):
    grid = [[1, 0, 1],
            [1, 0, 0],
            [0, 0, 0]]

    def test_neighbours(self):
        self.assertEqual(num_neigh(self.grid,2,2), 0)

    def test_should_die(self):
        self.assertEqual(should_die(self.grid, 2, 2), True)

if __name__ == '__main__':
    unittest.main()
