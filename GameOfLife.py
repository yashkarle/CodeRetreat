import unittest

def num_neigh(grid, x, y):
    iterators = [-1,0,1]
    sum = 0
    for i in iterators:
        for j in iterators:
            if 0<x+i<len(grid) and 0<y+j<len(grid):
                sum = sum + grid[y+j][x+i]
    return sum - grid[y][x]


class TestStringMethods(unittest.TestCase):

    def test_neighbours(self):
        grid=[[1,0,1],
              [1,0,0],
              [0,0,0]]
        self.assertEqual(num_neigh(grid,2,2), 0)


if __name__ == '__main__':
    unittest.main()
