"""Celebrity Problem
"""

from random import randrange


class CelebrityProblem:
    """solve Celebrity Problem by decrease-and-conquer"""
    def __init__(self, n):
        self.group = [i for i in range(n)]
        self.celebrity = randrange(n)
        print('group     =', self.group)
        print('celebrity =', self.celebrity, '\n')

    def solve(self):
        """solve"""
        if len(self.group) <= 1:
            return self.group[0]

        a, b = self.group[:2]
        answer = self._ask(a, b)
        if answer:
            self.group.remove(a)
        else:
            self.group.remove(b)
        print(f'{a:d} knows {b:d} ? {str(answer):5s}', self.group)

        return self.solve()

    def _ask(self, a, b):
        """ask A if he knows B"""
        return True if b == self.celebrity else False


print('\nresult =', CelebrityProblem(10).solve())
