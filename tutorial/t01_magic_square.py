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
                # horizontal check
                if sum(pattern[n*i:n*(i+1)]) != total:
                    break
            else:
                for i in range(n):
                    # vertical check
                    if sum(pattern[i:n*n:n]) != total:
                        break
                else:
                    # diagonal check
                    lower_right = sum([pattern[i*(n+1)] for i in range(n)])
                    upper_right = sum([pattern[(n-1-i)*n+i] for i in range(n)])
                    if total != lower_right or total != upper_right:
                        continue

                    # print pattern
                    for i in range(n):
                        print(pattern[i*n:(i+1)*n])
                    print()

                    self.count += 1

        return self.count


print('count =', MagicSquare(3).solve())
