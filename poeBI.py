import random

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def make_move(self, row, col):
        self.board[row][col] = self.current_player
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def make_computer_move(self):
        player_wins = self.find_winning_moves('X')
        if player_wins:
            row, col = random.choice(player_wins)
            self.make_move(row, col)
        else:
            computer_wins = self.find_winning_moves('O')
            if computer_wins:
                row, col = random.choice(computer_wins)
                self.make_move(row, col)
            else:
                best_move = self.bidirectional_search()
                if best_move:
                    row, col = best_move
                    self.make_move(row, col)
                else:
                    # If no winning move found, make a random move
                    row, col = random.choice(self.get_available_moves())
                    self.make_move(row, col)

    def find_winning_moves(self, player):
        winning_moves = []

        for row in range(3):
            for col in range(3):
                if self.board[row][col] == ' ':
                    self.board[row][col] = player

                    if self.check_winner(player):
                        winning_moves.append((row, col))

                    self.board[row][col] = ' '

        return winning_moves

    def bidirectional_search(self):
        available_moves = self.get_available_moves()

        for move in available_moves:
            row, col = move
            self.board[row][col] = 'O'

            if self.check_winner('O'):
                return move

            self.board[row][col] = ' '

        for move in available_moves:
            row, col = move
            self.board[row][col] = 'X'

            if self.check_winner('X') or self.bidirectional_search_helper('O'):
                self.board[row][col] = ' '
                return move

            self.board[row][col] = ' '

        return None

    def bidirectional_search_helper(self, player):
        if self.check_winner(player):
            return True

        available_moves = self.get_available_moves()

        for move in available_moves:
            row, col = move
            self.board[row][col] = player

            if player == 'O':
                if not self.bidirectional_search_helper('X'):
                    self.board[row][col] = ' '
                    return False
            else:
                if self.bidirectional_search_helper('O'):
                    self.board[row][col] = ' '
                    return True

            self.board[row][col] = ' '

        if player == 'O':
            return True
        else:
            return False

    def get_available_moves(self):
        available_moves = []
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == ' ':
                    available_moves.append((row, col))
        return available_moves

    def check_winner(self, player):
        for row in self.board:
            if row[0] == row[1] == row[2] == player:
                return True

        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] == player:
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True

        return False

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def play(self):
        while True:
            self.print_board()

            if self.check_winner('X'):
                print("Game over. Player wins!")
                break

            if self.check_winner('O'):
                print("Game over. Computer wins!")
                break

            if len(self.get_available_moves()) == 0:
                print("Game over. It's a draw!")
                break

            if self.current_player == 'X':
                row = int(input("Enter the row (0-2): "))
                col = int(input("Enter the column (0-2): "))
                self.make_move(row, col)
            else:
                print("Computer's turn...")
                self.make_computer_move()

        self.print_board()


# Start the game
game = TicTacToe()
game.play()