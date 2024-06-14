board = {1: ' ', 2: ' ', 3: ' ',
        4: ' ', 5: ' ', 6: ' ',
        7: ' ', 8: ' ', 9: ' '}

def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print("\n")


def spaceIsFree(position):
    if (board[position] == ' '):
        return True
    else:
        return False


def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        printBoard(board)
        if (checkDraw()):
            print("Draw!")
            exit()
        if checkForWin():
            if letter == 'X':
                print("Bot wins!")
                exit()
            else:
                print("Player wins!")
                exit()

        return


    else:
        print("Can't insert there!")
        position = int(input("Please enter new position:  "))
        insertLetter(letter, position)
        return


def checkForWin():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False


def checkWhichMarkWon(mark):
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False


def checkDraw():
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True


def playerMove():
    position = int(input("Enter the position for 'O':  "))
    insertLetter(player, position)
    return

def heuristic(board):
  """Counts the number of empty spaces on the board.

  Args:
    board: A dictionary representing the current state of the game board.

  Returns:
    The number of empty spaces on the board.
  """

  empty_spaces = 0
  for key in board.keys():
    if board[key] == ' ':
      empty_spaces += 1
  return empty_spaces


def compMove():
  """Makes a move for the computer player using the UCS algorithm."""

  # Create a priority queue to store all of the possible moves.
  queue = []

  # Iterate over all of the empty spaces on the board.
  for key in board.keys():
    if board[key] == ' ':

      # Calculate the cost of the move.
      cost = heuristic(board)

      # Add the move to the priority queue.
      queue.append((cost, key))

  # Sort the priority queue by cost.
  queue.sort(key=lambda x: x[0])

  # Choose the move with the lowest cost.
  best_move = queue.pop(0)[1]

  # Insert the best move.
  insertLetter(bot, best_move)

def evaluate_board(board, maximizing_player):
  """Evaluates the current state of the game board and returns a score for the
  player who is trying to maximize their score.

  Args:
    board: A dictionary representing the current state of the game board.
    maximizing_player: A boolean value indicating whether the player is trying to
      maximize their score (True) or minimize their opponent's score (False).

  Returns:
    A score for the player who is trying to maximize their score.
  """

  # Check if the player has won.
  if checkWhichMarkWon(maximizing_player):
    return 100

  # Check if the opponent has won.
  elif checkWhichMarkWon(not maximizing_player):
    return -100

  # Otherwise, the game is tied or in progress.
  else:
    return 0

def ids_minimax(board, depth, maximizing_player, memo={}):
  """Performs an iterative deepening search of the minimax game tree with memoization.

  Args:
    board: A dictionary representing the current state of the game board.
    depth: The current depth of the search tree.
    maximizing_player: A boolean value indicating whether the current player is
      trying to maximize their score (True) or minimize their opponent's score
      (False).
    memo: A dictionary that stores the results of previous function calls.

  Returns:
    The best possible score for the current player, assuming that both players
    play optimally.
  """

  # Check if the result has already been calculated.
  if (board, depth, maximizing_player) in memo:
    return memo[(board, depth, maximizing_player)]

  # Calculate the result and store it in the memo.
  if depth == 0 or checkForWin():
    result = evaluate_board(board, maximizing_player)
  else:
    if maximizing_player:
      result = -800
      for key in board.keys():
        if board[key] == ' ':
          board[key] = bot
          score = ids_minimax(board, depth - 1, False, memo)
          board[key] = ' '
          result = max(result, score)
    else:
      result = 800
      for key in board.keys():
        if board[key] == ' ':
          board[key] = player
          score = ids_minimax(board, depth - 1, True, memo)
          board[key] = ' '
          result = min(result, score)

  memo[(board, depth, maximizing_player)] = result

  return result






printBoard(board)
print("Computer goes first! Good luck.")
print("Positions are as follow:")
print("1, 2, 3 ")
print("4, 5, 6 ")
print("7, 8, 9 ")
print("\n")
player = 'O'
bot = 'X'


global firstComputerMove
firstComputerMove = True

while not checkForWin():
    compMove()
    playerMove()