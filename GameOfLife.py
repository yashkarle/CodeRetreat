import unittest

def num_neigh(grid, x, y):
    return 0


class TestStringMethods(unittest.TestCase):

    def test_neighbours(self):
        grid=[]
        self.assertEqual(num_neigh(grid,0,0), 0)


if __name__ == '__main__':
    unittest.main()
