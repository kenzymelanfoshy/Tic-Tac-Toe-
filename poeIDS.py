import random

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def make_move(self, row, col):
        self.board[row][col] = self.current_player
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def make_computer_move(self):
        depth_limit = 1

        while True:
            best_move = self.dfs_search(self.board, depth_limit)
            if best_move:
                row, col = best_move
                self.make_move(row, col)
                break
            
            depth_limit += 1

    def dfs_search(self, board, depth_limit):
        available_moves = []
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    available_moves.append((row, col))

        best_move = None

        for move in available_moves:
            row, col = move
            board[row][col] = 'O'

            if self.depth_limited_dfs(board, depth_limit, False):
                best_move = move

            board[row][col] = ' '

        return best_move

    def depth_limited_dfs(self, board, depth_limit, is_maximizing):
        winner = self.check_winner(board)

        if winner == 'O':  # Computer wins
            return True
        elif winner == 'X':  # Player wins
            return False
        elif depth_limit == 0:  # Reached depth limit
            return False

        available_moves = []
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    available_moves.append((row, col))

        if is_maximizing:
            for move in available_moves:
                row, col = move
                board[row][col] = 'O'

                if self.depth_limited_dfs(board, depth_limit - 1, False):
                    board[row][col] = ' '
                    return True

                board[row][col] = ' '
        else:
            for move in available_moves:
                row, col = move
                board[row][col] = 'X'

                if self.depth_limited_dfs(board, depth_limit - 1, True):
                    board[row][col] = ' '
                    return False

                board[row][col] = ' '

        return not is_maximizing

    def check_winner(self, board):
        for row in board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]

        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] != ' ':
                return board[0][col]

        if board[0][0] == board[1][1] == board[2][2] != ' ':
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != ' ':
            return board[0][2]

        return None

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def play(self):
        while True:
            self.print_board()

            if self.check_winner(self.board) is not None:
                print("Game over. {} wins!".format(self.check_winner(self.board)))
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