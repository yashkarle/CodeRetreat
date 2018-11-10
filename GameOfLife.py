import unittest

def num_neigh(grid, x, y):
    iterators = [-1,0,1]
    sum = 0
    for i in iterators:
        for j in iterators:
            if 0<=x+i<len(grid) and 0<=y+j<len(grid):
                sum = sum + grid[y+j][x+i]
    return sum - grid[y][x]

def should_die(grid, x,y):
    if num_neigh(grid, x, y) < 2 or num_neigh(grid, x, y) > 4:
        return True
    else:
        return False

def should_live(grid, x, y):
    if 1 < num_neigh(grid ,x, y) < 5:
        return True
    else:
        return False

def is_new_born(grid, x, y):
    if num_neigh(grid, x, y) == 3:
        return True
    return False

def new_cell(grid, x, y):
    return 0

class TestStringMethods(unittest.TestCase):
    grid = [[1, 0, 1],
            [1, 0, 0],
            [0, 0, 0]]

    def test_neighbours(self):
        self.assertEqual(num_neigh(self.grid,1,1), 3)

    def test_should_die(self):
        self.assertEqual(should_die(self.grid, 2, 2), True)
        self.assertEqual(should_die(self.grid, 1, 1), False)
        self.assertEqual(should_die(self.grid, 0, 1), True)

    def test_should_live(self):
        self.assertEqual(should_live(self.grid, 0, 1), False)
        self.assertEqual(should_live(self.grid, 1, 1), True)
        # self.assertEqual(should_live(self.grid, 0, 1), False)


    def test_new_born(self):
        self.assertEqual(is_new_born(self.grid, 0, 0), False)

    def test_new_cell(self):
        self.assertEqual(new_cell(self.grid, 0, 0), 0)


if __name__ == '__main__':
    unittest.main()
