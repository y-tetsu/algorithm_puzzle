"""Optimal Pie Cutting
"""


class OptimalPieCutting:
    def __init__(self, n):
        print('-----')
        print('n =', n)
        self.n = n

    def solve(self):
        # Check all patterns
        n, max_pie = self.n, 0
        print('\n* check all patterns *')
        for h in range(n+1):
            v = n - h
            pie = (h + 1) * (v + 1)
            print(f' - h = {h}, v = {v}, pie = (h + 1) * (v + 1) = {pie}')
            max_pie = max(pie, max_pie)
        print('max_pie =', max_pie)

        # Solve a formula
        print('\n* solve a formula *')
        h = n // 2
        v = n - h
        max_pie = (h + 1) * (v + 1)
        print(f' - h = n // 2 = {h}')
        print(f' - v = n - h  = {v}')
        print(f'max_pie = (h + 1) * (v + 1) = {max_pie}')
        print()


if __name__ == '__main__':
    OptimalPieCutting(5).solve()
    OptimalPieCutting(10).solve()
