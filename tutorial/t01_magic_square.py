"""Magic Square
"""

import itertools


class MagicSquare:
    """magic square"""
    def __init__(self, n):
        self.n = n
        self.count = 0

    def solve(self):
        """solve"""
        n = self.n
        for pattern in itertools.permutations([i + 1 for i in range(n*n)], n*n):
            # initial
            total = sum([pattern[i] for i in range(0, n*n, n)])

            # horizontal
            horizontal = True
            for offset in range(n):
                if total != sum([pattern[offset*n + i] for i in range(n)]):
                    horizontal = False
                    break
            if not horizontal:
                continue

            # vertical
            vertical = True
            for offset in range(n):
                if total != sum([pattern[offset + i] for i in range(0, n*n, n)]):
                    vertical = False
                    break
            if not vertical:
                continue

            # diagonal
            diagonal = True
            if total != sum([pattern[i*n + i] for i in range(n)]):
                diagonal = False
            if total != sum([pattern[(n-1-i)*n + i] for i in range(n)]):
                diagonal = False
            if not diagonal:
                continue

            # result
            for i in range(n):
                print(pattern[i*n:(i+1)*n])
            print()
            self.count += 1

        return self.count


print('count =', MagicSquare(3).solve())
