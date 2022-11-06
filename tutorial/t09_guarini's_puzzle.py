"""Guarini's Puzzle
"""

EMPTY = 0
BLACK = 1
WHITE = 2


class GuarinisPuzzle:
    def __init__(self, black, white):
        self.route = {1: 8, 8: 3, 3: 4, 4: 9, 9: 2, 2: 7, 7: 6, 6: 1}
        self.board = [EMPTY for _ in range(9)]
        self.black = black
        self.white = white
        for i in black:
            self.board[i-1] = BLACK
        for i in white:
            self.board[i-1] = WHITE
        self.black_goal = [i for i in white]
        self.white_goal = [i for i in black]
        self.cnt = 0
        self.show_board()

    def show_board(self):
        line = []
        print(self.cnt)
        print('-------')
        for i, value in enumerate(self.board, 1):
            if value == EMPTY:
                line.append(' ')
            elif value == BLACK:
                line.append('B')
            elif value == WHITE:
                line.append('W')
            if i % 3 == 0:
                print('|' + '|'.join(line) + '|')
                print('-------')
                line = []
        print()

    def solve(self):
        while self.move():
            self.show_board()
        return self.cnt

    def move(self):
        route, board = self.route, self.board
        b = [self.black, self.black_goal, BLACK]
        w = [self.white, self.white_goal, WHITE]
        for color, goal, piece in [b, w]:
            for i in range(2):
                position = color[i]
                if position == goal[i]:
                    continue
                next_position = route[position]
                if board[next_position-1] != EMPTY:
                    continue
                board[next_position-1] = piece
                board[position-1] = EMPTY
                color[i] = next_position
                self.cnt += 1
                return True
        return False


print('result =', GuarinisPuzzle([1, 3], [9, 7]).solve())
