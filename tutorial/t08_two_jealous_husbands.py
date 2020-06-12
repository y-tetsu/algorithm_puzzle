"""Two Jealous Husbands
"""

import itertools
from collections import namedtuple


class TwoJealousHusbands:
    """solve Two Jealous Husbands by transform-and-concuer"""
    HUSBAND, WIFE, WEST, EAST = 'H', 'W', 0, 1
    Person = namedtuple('Person', 'relation num')
    State = namedtuple('State', 'shore boat memo path')

    def __init__(self, couple=2, capacity=2):
        self.couple = couple
        self.capacity = capacity
        west, east = [self.Person(i, j) for i in (self.HUSBAND, self.WIFE) for j in range(1, couple+1)], []
        memo = {}
        memo[(self.WEST, ''.join(sorted((i.relation + str(i.num) for i in west))))] = True
        self.queue = [[self.State([west, east], self.WEST, memo, [])]]
        self.results = []
        print('+' + '---'*couple*2 + '--------' + '--'*capacity + '+')
        print('|', *[i.relation + str(i.num) for i in west if i.relation == self.HUSBAND], '|<' + '[]'*capacity + '>  |' + '   '*couple + ' |')
        print('|', *[i.relation + str(i.num) for i in west if i.relation == self.WIFE], '|    ' + '  '*capacity + '|' + '   '*couple + ' |')
        print('+' + '---'*couple*2 + '--------' + '--'*capacity + '+')

    def solve(self):
        """solve"""
        solutions = []
        while self.queue:
            states, next_states = self.queue.pop(0), []
            for state in states:
                if self._goal(state):
                    solutions.append(state)
                else:
                    next_states.extend(self._cross(state))

            if solutions:
                break

            if next_states:
                self.queue.append(next_states)

        result = ''
        if solutions:
            result += 'crossing river   = ' + str(len(solutions[0].path)) + '\n'
            result += 'optimal solution = ' + str(len(solutions)) + '\n\n'
            result += '\n'.join([' -> '.join(i.path) for i in reversed(solutions)])
        else:
            result += 'crossing river   = 0\n'
            result += 'optimal solution = 0'

        return result

    def _goal(self, state):
        """goal"""
        return True if len(state.shore[self.EAST]) == self.couple*2 else False

    def _cross(self, state):
        """Persons cross the river by boat"""
        next_states = []
        boat, next_boat = state.boat, (state.boat + 1) % 2
        for i in range(self.capacity):
            for persons in itertools.combinations(state.shore[boat], i+1):
                next_shore = [i[:] for i in state.shore]
                for person in persons:  # persons cross the river
                    next_shore[next_boat] += [next_shore[boat].pop(next_shore[boat].index(person))]

                next_path = ''.join(sorted([i.relation + str(i.num) for i in persons]))
                memo = (next_boat, ''.join(sorted((i.relation + str(i.num) for i in next_shore[self.WEST]))))
                if memo not in state.memo:
                    next_memo = state.memo.copy()
                    next_memo[memo] = True
                    next_state = self.State(next_shore, next_boat, next_memo, state.path + [next_path])
                    if not self._not_like(next_state):  # check husbands's feeling
                        next_states += [next_state]

        return self._exclude_symmetry(next_states)

    def _not_like(self, state):
        """A Husband does not like his wife to be with other husbands when he is not"""
        for here in [self.WEST, self.EAST]:
            over = (here + 1) % 2
            for me in state.shore[here]:
                if me.relation == self.HUSBAND:
                    my_wife = [True for i in state.shore[over] if i.relation == self.WIFE and i.num == me.num]
                    other_husband = [True for i in state.shore[over] if i.relation == self.HUSBAND]
                    if my_wife and other_husband:
                        return True

        return False

    def _exclude_symmetry(self, states):
        """Exclude symmetry"""
        excluded = states[:]
        if excluded:
            for crossing in range(len(excluded[0].path)):
                excluded, tmp = sorted(excluded, key=lambda x:''.join(x.path), reverse=(crossing+1)%2 == 0), []
                for index1 in range(len(excluded)):
                    for index2 in range(index1+1, len(excluded)):
                        if self._is_symmetry(excluded, crossing, index1, index2):
                            break
                    else:
                        tmp.append(excluded[index1])

                excluded = tmp[:]

        return excluded

    def _is_symmetry(self, excluded, crossing, index1, index2):
        """return True if pattern is symmetry"""
        pre_path = ''.join([excluded[index1].path[i] for i in range(crossing)])
        if not pre_path or pre_path == ''.join([excluded[index2].path[i] for i in range(crossing)]):
            org = tuple([i for i in range(1, self.couple+1)])
            symmetry_paths = []
            for ptn in itertools.permutations(range(1, self.couple+1)):
                if org != ptn:
                    symmetry_path = excluded[index1].path[crossing]
                    for i in range(self.couple):
                        symmetry_path = symmetry_path.replace(str(org[i]), str(org[i]+self.couple))

                    for i in range(self.couple):
                        symmetry_path = symmetry_path.replace(str(org[i]+self.couple), str(ptn[i]))

                    symmetry_path = ''.join(sorted([symmetry_path[i: i+2] for i in range(0, len(symmetry_path), 2)]))
                    if excluded[index1].path[crossing] != symmetry_path and symmetry_path not in symmetry_paths:
                        symmetry_paths.append(symmetry_path)

            if excluded[index2].path[crossing] in symmetry_paths:
                return True

        return False


print(TwoJealousHusbands().solve(), '\n')
print(TwoJealousHusbands(3, 2).solve(), '\n')
print(TwoJealousHusbands(3, 3).solve())
