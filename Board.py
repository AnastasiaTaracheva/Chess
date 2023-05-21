from Piece import *
from Pawn import Pawn


class Board:
    def __init__(self):
        self.color = WHITE
        self.field = []
        for row in range(8):
            self.field.append([None] * 8)
        for col in range(8):
            self.field[1][col] = Pawn(1, col, WHITE)
            self.field[6][col] = Pawn(6, col, BLACK)

    def correct_coords(self, row, col):
        """
        Функция проверяет, что координата(row, col) лежит внутри доски
        """
        return 0 <= row <= 8 and 0 <= col <= 8

    def is_under_attack(self, row, col, color):
        for i in range(8):
            for j in range(8):
                if self.field[i][j] if not None:
                    piece = self.field[i][j]
                    if piece.get_color() == color:
                        if piece.can_move(row, col):
                            return True
        return False

    def show_board(self):
        print('       +----+----+----+----+----+----+----+----')
        for row in range(7, -1, -1):
            print(' ', row, end=' ')
            for col in range(8):
                print('|', self.field[row][col], end=' ')
            print('|')
            print('       +----+----+----+----+----+----+----+----')
        print(end='    ')
        for col in range(8):
            print(col, end='    ')
        print()

    def current_player_color(self):
        return self.color

    def cell(self, row, col):
        piece = self.field[row][col]
        if piece == None:
            return ' '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()

    def move(self, row, col, row_to, col_to):
        if self.correct_coords(row, col) or \
                not self.correct_coords(row_to, col_to):
            return False
        if row == row_to and col == col_to:
            return False
        piece = self.field[row][col]
        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False
        if not piece.can_move(row_to, col_to):
            return False
        self.field[row][col] = None
        self.field[row_to][col_to] = piece
        piece.set_position(row_to, col_to)
        self.color = piece.opponent()
        return True