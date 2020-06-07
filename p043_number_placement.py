"""Number Placement
"""

import random


class NumberPlacement:
    """solve Number Placement"""
    MAX_NUMBER = 100

    def __init__(self, n):
        self.numbers = random.sample(range(self.MAX_NUMBER), n)
        self.inequalities = random.choices(['<', '>'], k=n-1)
        print('numbers =', *self.numbers)
        print('boxes   =', *self.inequalities, '',  sep=' [] ')

    def solve(self):
        """solve"""
        result = []
        numbers = sorted(self.numbers)
        for inequality in self.inequalities:
            if inequality == '<':
                result.append(numbers.pop(0))
                result.append('<')
            else:
                result.append(numbers.pop())
                result.append('>')

        result.append(numbers.pop(0))

        return result


print('result  =', *NumberPlacement(4).solve(), '\n')
print('result  =', *NumberPlacement(10).solve())
