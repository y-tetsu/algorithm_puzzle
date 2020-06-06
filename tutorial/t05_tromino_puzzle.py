"""Tromino Puzzle
"""

from random import randrange


class TrominoPuzzle:
    """solve Tromino Puzzle by divide-and-conquer"""
    BLANK = 10

    def __init__(self, n):
        self.size = 2 ** n
        self.board = [-1 for i in range(self.size**2)]
        self.board[randrange(self.size**2)] = self.count = self.BLANK  # one missing square

    def solve(self, board=None):
        """solve"""
        board = self.board[:] if not board else board
        size = int(len(board) ** 0.5)

        tl, tr, bl, br = self._divide(size, board)
        self._place(size//2, tl, tr, bl, br)

        if size == 2:
            return self._merge(size//2, tl, tr, bl, br)
        else:
            board = self._merge(size//2, self.solve(tl), self.solve(tr), self.solve(bl), self.solve(br))

        if size == self.size:
            print('(Initial)', *[self.board[size*i:size*(i+1)] for i in range(size)], '', sep='\n')
            print('(Result)', *[board[size*i:size*(i+1)] for i in range(size)], sep='\n')

        return board

    def _divide(self, size, board):
        """divide board into four"""
        p_size = size // 2
        topleft, topright, bottomleft, bottomright = [], [], [], []
        for i in range(p_size):
            j = i + p_size
            topleft += board[size*i:size*i+p_size]
            topright += board[size*i+p_size:size*(i+1)]
            bottomleft += board[size*j:size*j+p_size]
            bottomright += board[size*j+p_size:size*(j+1)]

        return topleft, topright, bottomleft, bottomright

    def _merge(self, size, topleft, topright, bottomleft, bottomright):
        """merge four divided board"""
        b_size = size * 2
        board = [-1 for i in range(b_size**2)]
        for i in range(size):
            j = i + size
            board[b_size*i:b_size*i+size] = topleft[size*i:size*(i+1)]
            board[b_size*i+size:b_size*i+size*2] = topright[size*i:size*(i+1)]
            board[b_size*j:b_size*j+size] = bottomleft[size*i:size*(i+1)]
            board[b_size*j+size:b_size*j+size*2] = bottomright[size*i:size*(i+1)]

        return board

    def _place(self, size, topleft, topright, bottomleft, bottomright):
        """Place the tromino in the center of the board.
           However, place it so as to avoid the place containing tromino
           on the board divided into four.
        """
        self.count += 1
        for part, index in [(topleft, -1), (topright, -size), (bottomleft, size-1), (bottomright, 0)]:
            part[index] = part[index] if self._has_tromino(part, self.count) else self.count

    def _has_tromino(self, part, count):
        """return if part has tromino"""
        return not set(range(self.BLANK, count)).isdisjoint(set(part))


TrominoPuzzle(3).solve()
