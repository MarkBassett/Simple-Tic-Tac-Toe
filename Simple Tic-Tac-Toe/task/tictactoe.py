class Game:
    def __init__(self):
        self.board = [[' ' for col in range(3)] for row in range(3)]
        self.pieces = ['X', 'O']
        self.win = []
        self.no_pieces = []
        self.play = True
        self.player_piece = 0

    def game_analysis(self):
        for piece in self.pieces:
            piece_total = 0
            for row in self.board:
                piece_total += row.count(piece)
                if row.count(piece) == 3:
                    self.win.append(piece)
            for col in range(3):
                veritical = [self.board[row][col] for row in range(3)]
                if veritical.count(piece) == 3:
                    self.win.append(piece)
            if self.board[0][0] == piece and self.board[1][1] == piece and self.board[2][2] == piece:
                self.win.append(piece)
            if self.board[0][2] == piece and self.board[1][1] == piece and self.board[2][0] == piece:
                self.win.append(piece)
            self.no_pieces.append(piece_total)
        empty_cells = [col for row in self.board for col in row if col == ' ']
        if len(self.win) > 1 or abs(self.no_pieces[0] - self.no_pieces[1]) > 1:
            print('Impossible')
            self.play = False
        elif len(self.win) == 1:
            print(f'{self.win[0]} wins')
            self.play = False
        elif not empty_cells:
            print('Draw')
            self.play = False

    def display_board(self):
        print('-' * 9)
        for row in self.board:
            print('|', end=' ')
            for col in row:
                print(col, end=' ')
            print('|')
        print('-' * 9)

    def user_move(self, move):
        row, col = move.split()
        if row.isalpha() or col.isalpha():
            print('You should enter numbers!')
        else:
            row, col = [int(n) - 1 for n in move.split()]
            if 0 <= row >= 3 or 0 <= col >= 3:
                print('Coordinates should be from 1 to 3!')
            elif self.board[row][col] in self.pieces:
                print('This cell is occupied! Choose another one!')
            else:
                self.board[row][col] = self.pieces[self.player_piece]
                self.player_piece = not self.player_piece
                self.display_board()
                self.game_analysis()

my_game = Game()
my_game.display_board()
while my_game.play:
    my_game.user_move(input())