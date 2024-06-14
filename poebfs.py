from collections import deque
import random

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def make_move(self, row, col):
        self.board[row][col] = self.current_player
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def make_computer_move(self):
        queue = deque()
        visited = set()

        # Start BFS from the current board state
        queue.append((self.board, []))
        visited.add(tuple(map(tuple, self.board)))

        while queue:
            board, path = queue.popleft()

            if self.check_winner(board) == 'O':
                # Computer wins, stop the search
                move = path[0]
                row, col = move
                self.make_move(row, col)
                return

            # Get all available moves
            available_moves = []
            for row in range(3):
                for col in range(3):
                    if board[row][col] == ' ':
                        available_moves.append((row, col))

            for move in available_moves:
                new_board = [row[:] for row in board]
                row, col = move
                new_board[row][col] = 'O'

                if tuple(map(tuple, new_board)) not in visited:
                    queue.append((new_board, path + [move]))
                    visited.add(tuple(map(tuple, new_board)))

        # If no winning move found, make a random move
        row, col = random.choice(available_moves)
        self.make_move(row, col)

    def check_winner(self, board):
        # Check rows
        for row in board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]

        # Check columns
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] != ' ':
                return board[0][col]

        # Check diagonals
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