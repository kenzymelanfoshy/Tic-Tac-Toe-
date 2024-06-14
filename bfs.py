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


def compMove():
    bestScore = -800
    bestMove = 0
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = bot
            score = bfs_minimax(board, 0, False)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key

    insertLetter(bot, bestMove)
    return


def bfs_minimax(board, depth, maximizing_player):
  """Performs a breadth-first search of the minimax game tree.

  Args:
    board: A dictionary representing the current state of the game board.
    depth: The current depth of the search tree.
    maximizing_player: A boolean value indicating whether the current player is
      trying to maximize their score (True) or minimize their opponent's score
      (False).

  Returns:
    The best possible score for the current player, assuming that both players
    play optimally.
  """

  # Create a queue to store the nodes that need to be explored.
  queue = []
  queue.append((board, depth, maximizing_player))

  # While the queue is not empty, explore the nodes in the queue.
  while queue:
    board, depth, maximizing_player = queue.pop(0)

    # If we have reached the end of the game tree, return the value of the
    # current state.
    #if depth == 0 or checkWhichMarkWon(board):
   #   return evaluate_board(board, maximizing_player)

    # If we are the maximizing player, add all possible moves to the queue.
    if maximizing_player:
      for key in board:
        if board[key] == ' ':
          board[key] = bot
          queue.append((board.copy(), depth - 1, False))
          board[key] = ' '

    # If we are the minimizing player, add all possible moves to the queue, but
    # in reverse order. This will ensure that the worst possible move for the
    # opponent is explored first.
    else:
      for key in board:
        if board[key] == ' ':
          board[key] = player
          queue.append((board.copy(), depth - 1, True))
          board[key] = ' '

  # If we reach this point, the queue is empty and we have explored all possible
  # moves. Return the best possible score for the current player
  return best_score



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