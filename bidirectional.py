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

import copy

def bidirectional_search(board, goal_state):
  """Performs a bidirectional search for a solution to the Tic-Tac-Toe game.

  Args:
    board: A dictionary representing the current state of the game board.
    goal_state: The goal state of the game board.

  Returns:
    A list of moves that lead from the initial state to the goal state, or None
    if no solution is found.
  """

  # Create two priority queues, one for the forward search and one for the backward
  # search.
  forward_queue = []
  backward_queue = []

  # Add the initial state to the forward queue.
  forward_queue.append((board, []))

  # Add the goal state to the backward queue.
  backward_queue.append((goal_state, []))

  # While neither queue is empty:
  while forward_queue and backward_queue:

    # Pop the first state from the forward queue.
    current_state, forward_moves = forward_queue.pop(0)

    # Expand the state and add all of its children to the forward queue, if they are
    # not already in the queue.
    children = expand_state(current_state)
    for child in children:
      if child not in forward_queue and child not in backward_queue:
        forward_queue.append((child, forward_moves + [child]))

      # If any of the children are in the backward queue, then we have found a
      # solution and we can stop.
      if child in backward_queue:
        backward_moves = backward_queue.pop(0)[1]
        return forward_moves + backward_moves[::-1]

    # Pop the first state from the backward queue.
    current_state, backward_moves = backward_queue.pop(0)

    # Expand the state and add all of its parents to the backward queue, if they are
    # not already in the queue.
    parents = expand_state(current_state, reverse=True)
    for parent in parents:
      if parent not in forward_queue and parent not in backward_queue:
        backward_queue.append((parent, [parent] + backward_moves))

      # If any of the parents are in the forward queue, then we have found a
      # solution and we can stop.
      if parent in forward_queue:
        forward_moves = forward_queue.pop(0)[1]
        return forward_moves + backward_moves[::-1]

  # If we reach here, then no solution was found.
  return None


def expand_state(state, reverse=False):
  """Expands a Tic-Tac-Toe state by generating all of its possible children.

  Args:
    state: A dictionary representing the current state of the game board.
    reverse: A boolean value indicating whether to expand the state forward (False)
      or backward (True).

  Returns:
    A list of all of the children of the given state.
  """

  children = []
  for position in range(1, 10):
    if state[position] == ' ':
      new_state = copy.deepcopy(state)
      if reverse:
        new_state[position] = 'O'
      else:
        new_state[position] = 'X'
      children.append(new_state)
  return children






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