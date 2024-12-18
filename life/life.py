import numpy as np # noqa d100
from matplotlib import pyplot
from scipy.signal import convolve2d

glider = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]])

# and we go again again

blinker = np.array([
 [0, 0, 0],
 [1, 1, 1],
 [0, 0, 0]]
)

glider_gun = np.array([
    [0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0]
])


class Game:
    """Cellular Automata Game."""

    def __init__(self, size):
        """Construct method."""
        self.board = np.zeros((size, size))

    def play(self):
        """Playing the game."""
        print("Playing life. Press ctrl + c to stop.")
        pyplot.ion()
        while True:
            self.move()
            self.show()
            pyplot.pause(0.0000005)

    def move(self):
        """Move in the game."""
        stencil = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
        neighbourcount = convolve2d(self.board, stencil, mode='same')

        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                self.board[i, j] = 1 if (neighbourcount[i, j] == 3
                                         or (neighbourcount[i, j] == 2
                                         and self.board[i, j])) else 0

    def __setitem__(self, key, value):
        """Set items."""
        self.board[key] = value

    def show(self):
        """Show in the game."""
        pyplot.clf()
        pyplot.matshow(self.board, fignum=0, cmap='binary')
        pyplot.show()

    def insert(self, pattern, location):
        """Insert pattern onto game board."""
        self.board[location[0], location[1]] = pattern.grid[1, 1]
        self.board[location[0], location[1]] = pattern.grid[1, 1]
        self.board[location[0] - 1, location[1] - 1] = pattern.grid[0, 0]
        self.board[location[0] - 1, location[1]] = pattern.grid[0, 1]
        self.board[location[0] - 1, location[1] + 1] = pattern.grid[0, 2]
        self.board[location[0], location[1] - 1] = pattern.grid[1, 0]
        self.board[location[0], location[1] + 1] = pattern.grid[1, 2]
        self.board[location[0] + 1, location[1] - 1] = pattern.grid[2, 0]
        self.board[location[0] + 1, location[1]] = pattern.grid[2, 1]
        self.board[location[0] + 1, location[1] + 1] = pattern.grid[2, 2]


class Pattern:
    """Pattern class."""

    def __init__(self, array):
        """Construct method."""
        self.grid = array

    def __repr__(self):
        """Return a string representation of the pattern's grid."""
        return f"{self.grid}"

    def flip_vertical(self):
        """Return flipped pattern in vertical axis."""
        return Pattern(np.flipud(self.grid))

    def flip_horizontal(self):
        """Return flipped pattern in horizontal axis."""
        return Pattern(np.fliplr(self.grid))

    def flip_diag(self):
        """Return the transpose of a pattern."""
        return Pattern(np.transpose(self.grid))

    def rotate(self, n):
        """Rotate a pattern through n right anticlockwise turns."""
        lizst = [self.grid]
        for i in range(n):
            temp = np.flipud(np.transpose(lizst[-1]))
            lizst.append(temp)
        return Pattern(lizst[-1])


A = Pattern(np.diag([1.0, 2, 3]))
print(np.zeros((9, 9)))
