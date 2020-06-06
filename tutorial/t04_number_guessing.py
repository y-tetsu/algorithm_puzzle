"""Number Guessing
"""

from math import ceil
from random import randint


class NumberGuessing:
    """solve Number Guessing by decrease-and-conquer"""
    def __init__(self, n):
        self.n = n
        self.number = randint(1, n)
        self.count = 0
        print('n =', self.n, 'number =', self.number, '\n')

    def solve(self, low=None, high=None):
        """solve"""
        low, high = low if low else 1, high if high else self.n
        if low == high:
            return low

        n = high + low - 1
        q = ceil(n/2)
        answer = self._ask_greater(q)
        self.count += 1
        print('{:>2d}'.format(self.count), 'greater than', q, '?', answer)

        return self.solve(q+1, high) if answer else self.solve(low, q)

    def _ask_greater(self, question):
        """Ask if correct answer is greater than Question"""
        return True if question < self.number else False


print('\nresult =', NumberGuessing(10).solve(), '\n')
print('\nresult =', NumberGuessing(1000000).solve(), '\n')
