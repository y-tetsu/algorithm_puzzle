"""Magic Square
"""

import itertools


class MagicSquare:
    """solve Magic Square"""
    def __init__(self, n):
        self.n = n
        self.count = 0

    def solve(self):
        """solve"""
        n = self.n
        for pattern in itertools.permutations([i + 1 for i in range(n*n)], n*n):
            total = sum(pattern[:n])
            for i in range(n):
                if sum(pattern[n*i:n*(i+1)]) != total:  # horizontal
                    break
            else:
                for i in range(n):
                    if sum(pattern[i:n*n:n]) != total:  # vertical
                        break
                else:
                    lower_right = sum([pattern[i*(n+1)] for i in range(n)])
                    upper_right = sum([pattern[(n-1-i)*n+i] for i in range(n)])
                    if total == lower_right == upper_right:  # diagonal
                        self.count += 1
                        print(*[pattern[i*n:(i+1)*n] for i in range(n)], '', sep='\n')

        return self.count


print('count =', MagicSquare(3).solve())
