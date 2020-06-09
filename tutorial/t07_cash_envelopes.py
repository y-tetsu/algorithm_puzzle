"""Cash Envelopes
"""

import itertools


class CashEnvelopes:
    """solve Cash Envelopes by transform-and-concuer"""
    def __init__(self, num, money):
        self.num = num
        self.money = money
        self.envelopes = [2**i for i in range(num-1)]
        last = money - sum(self.envelopes)
        self.envelopes += [last] if last > 0 else [0]
        print('money     =', money, '\nenvelopes =', self.envelopes, '\n')

    def solve(self):
        """solve"""
        count = 0
        for pattern in itertools.product([0, 1], repeat=self.num):
            pattern = list(reversed(pattern))
            total = sum([self.envelopes[i] for i in range(self.num) if pattern[i]])
            if total < self.envelopes[-1] or pattern[-1]:
                if 0 < total <= self.money:
                    print(f'({count:>4d})', 'pattern =', pattern, f'total = {total:>4d}', '!!! Error !!!' if total != count else '')

                count += 1


CashEnvelopes(10, 1000).solve()
