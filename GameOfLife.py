class GameOfLife:
    def __init__(self):
        self.board = [[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]]
        self.height = len(self.board)
        self.width = len(self.board[0])

    # returns the value at the cell (x,y)
    def get_cell_value(self, x, y):
        return self.board[x][y]

    # sets the cell value at (x,y)
    def set_cell_value(self, x, y, val):
        self.board[x][y] = val

    # we plan to calculate count of live neighbours
    def get_live_neighbours_count(self, x, y):
        count = 0
        iterator = [-1, 0, 1]

        for i in iterator:
            for j in iterator:
                if (0 <= (x+i) < self.width) and (0 <= (y+j) < self.height) and self.get_cell_value(x+i, y+j):
                    count += 1

        return count - self.get_cell_value(x, y)

    # calculates the new cell values depending upon the rules of the game
    def get_new_cell_value(self, x, y):
        num_live_neighbours = self.get_live_neighbours_count(x, y)

        if num_live_neighbours == 3 or (num_live_neighbours == 2 and self.get_cell_value(x, y)):
            return 1
        return 0

    # print the board
    def print_board(self):
        for i in range(self.width):
            for j in range(self.height):
                if self.get_cell_value(i, j):
                    print("X", end=" ")
                else:
                    print("O", end=" ")
            print()


if __name__ == '__main__':
    g = GameOfLife()
    g.set_cell_value(0, 0, 0)
    g.set_cell_value(0, 1, 1)
    g.set_cell_value(0, 2, 0)
    g.set_cell_value(1, 0, 0)
    g.set_cell_value(1, 1, 1)
    g.set_cell_value(1, 2, 0)
    g.set_cell_value(2, 0, 0)
    g.set_cell_value(2, 1, 1)
    g.set_cell_value(2, 2, 0)
    g.print_board()

    print()

    result = GameOfLife()
    result.set_cell_value(0, 0, g.get_new_cell_value(0, 0))
    result.set_cell_value(0, 1, g.get_new_cell_value(0, 1))
    result.set_cell_value(0, 2, g.get_new_cell_value(0, 2))
    result.set_cell_value(1, 0, g.get_new_cell_value(1, 0))
    result.set_cell_value(1, 1, g.get_new_cell_value(1, 1))
    result.set_cell_value(1, 2, g.get_new_cell_value(1, 2))
    result.set_cell_value(2, 0, g.get_new_cell_value(2, 0))
    result.set_cell_value(2, 1, g.get_new_cell_value(2, 1))
    result.set_cell_value(2, 2, g.get_new_cell_value(2, 2))
    result.print_board()
