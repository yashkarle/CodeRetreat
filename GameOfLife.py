import unittest

def num_neigh(grid, x, y):
    iterators = [-1,0,1]

    
    return 0


class TestStringMethods(unittest.TestCase):

    def test_neighbours(self):
        grid=[[1,0,1],
              [1,0,0],
              [0,0,0]]
        self.assertEqual(num_neigh(grid,2,2), 0)


if __name__ == '__main__':
    unittest.main()
