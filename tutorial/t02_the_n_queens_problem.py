"""The n-Queens Problem
"""


class nQueen:
    """The n-Queens Problem by backtracking"""
    def __init__(self, n):
        self.n = n
        self.directions = [
            (-1, 1),  (0, 1),  (1, 1),
            (-1, 0),           (1, 0),
            (-1, -1), (0, -1), (1, -1),
        ]
        self.board = ['_' for i in range(n*n)]
        self.control = [0 for i in range(n*n)]

    def backtracking(self, x=0):
        """backtracking"""
        n = self.n
        if x >= n:
            for i in range(n):
                print(self.board[n*i:n*(i+1)])
            print()
            return 1
        else:
            count = 0
            for y in [i for (i, v) in enumerate(self.control[x:n*n:n]) if v == 0]:
                self._put(x, y)
                count += self.backtracking(x+1)
                self._remove(x, y)
            return count

    def _put(self, x, y):
        """put queen"""
        self.board[x+y*self.n] = 'Q'
        self._update_control(x, y, 1)

    def _remove(self, x, y):
        """remove queen"""
        self.board[x+y*self.n] = '_'
        self._update_control(x, y, -1)

    def _update_control(self, x, y, delta):
        """update queen control"""
        n = self.n
        index = x + y * n
        self.control[index] += delta
        for dx, dy in self.directions:
            next_index, next_x, next_y = index, x, y
            while True:
                next_x += dx
                next_y += dy
                if 0 <= next_x < n and 0 <= next_y < n:
                    next_index += dx + dy * n
                    self.control[next_index] += delta
                else:
                    break


print('(N=4) count =', nQueen(4).backtracking(), '\n')
print('(N=8) count =', nQueen(8).backtracking(), '\n')
