"""The n-Queens Problem
"""

N = 4


class nQueen:
    """The n-Queens Problem by backtracking"""
    def __init__(self, n):
        self.directions = [
            (-1, 1),  (0, 1),  (1, 1),
            (-1, 0),           (1, 0),
            (-1, -1), (0, -1), (1, -1),
        ]
        self.board = ['_' for i in range(n*n)]
        self.control = [0 for i in range(n*n)]

    def backtracking(self, x=0):
        """backtracking"""
        if x >= N:
            for i in range(N):
                print(self.board[N*i:N*(i+1)])
            print()
            return 1
        else:
            cnt = 0
            for y in [i for (i, v) in enumerate(self.control[x:N*N:N]) if v == 0]:
                self._put(x, y)
                cnt += self.backtracking(x+1)
                self._remove(x, y)
            return cnt

    def _put(self, x, y):
        """put queen"""
        self.board[x+y*N] = 'Q'
        self._update_control(x, y, 1)

    def _remove(self, x, y):
        """remove queen"""
        self.board[x+y*N] = '_'
        self._update_control(x, y, -1)

    def _update_control(self, x, y, delta):
        """update queen control"""
        index = x + y * N
        self.control[index] += delta
        for dx, dy in self.directions:
            next_index, next_x, next_y = index, x, y
            while True:
                next_x += dx
                next_y += dy
                if 0 <= next_x < N and 0 <= next_y < N:
                    next_index += dx + dy * N
                    self.control[next_index] += delta
                else:
                    break


print('cnt =', nQueen(N).backtracking())
