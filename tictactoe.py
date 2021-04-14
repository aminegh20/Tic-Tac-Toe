"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
  """
  Returns starting state of the board.
  """
  return [[EMPTY, EMPTY, EMPTY],
      [EMPTY, EMPTY, EMPTY],
      [EMPTY, EMPTY, EMPTY]]


def player(board):
  """
  Returns player who has the next turn on a board.
  """

  #check for terminal board
  if terminal(board): return None 

  #count total moves made by both players
  count_moves_made = 0  
  for rows in board:
    for move in rows:
      if move != EMPTY:
        count_moves_made += 1

  #even --> X
  #odd  --> O
  if count_moves_made % 2 == 0:   
    return X
  else:                         
    return O

def actions(board):
  """
  Returns set of all possible actions (i, j) available on the board.
  """

  #check for terminal board
  if terminal(board): return None   

  #store possible actions
  possible_actions = set()   

  #if a cell is not empty, then a move can be made
  for i in range(3):
    for j in range(3):
      if board[i][j] == EMPTY:
        possible_actions.add((i, j))                     
  return possible_actions


def result(board, action):
  """
  Returns the board that results from making move (i, j) on the board.
  """
         
  i, j = action                                         
  if board[i][j] is EMPTY:
    player_turn = player(board)
    new_board = deepcopy(board) 
    new_board[i][j] = player_turn
    return new_board
  else:
    raise Exception("Invalid Move")


def winner(board):
  """
  Returns the winner of the game, if there is one.
  """
  
  #check diogonally
  if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != EMPTY:
    return board[0][0]

  elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != EMPTY:
    return board[2][0]
  
  #check rows
  for row in board:
    if row[0] == row[1] and row[1] == row[2] and row[0] != EMPTY:
      return row[0]

  #check columns
  for i in range(3):
    if board[0][i] == board[1][i] and board [1][i] == board[2][i] and board[0][i] != EMPTY:
      return board[0][i]

  return None


def terminal(board):
  """
  Returns True if game is over, False otherwise.
  """

  if winner(board) != None:     
    return True
  for rows in board:
    for moves in rows:
      if moves == EMPTY:
        return False
  return True
  

def utility(board):
  """
  Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
  """
  win = winner(board)
  if win == X:
    return 1
  elif win == O:
    return -1
  else:
    return 0


# naive !! to - be fixed
def minimax(board):
  """
  Returns the optimal action for the current player on the board.
  """
  if terminal(board): return None
  best_move = (-1, -1)
  if player(board) == X:
    v = -1
    for action in actions(board):
      value = min_value(result(board, action))
      if value == 1:
        return action
      if value > v:
        v = value
        best_move = action
  else:
    v = 1
    for action in actions(board):
      value = max_value(result(board, action))
      if value == -1:
        return action
      if v > value:
        v = value
        best_move = action

  return best_move
  

def max_value(board):

  if terminal(board):
    return utility(board)
  v = -1

  for action in actions(board):
    v = max(v, min_value(result(board, action)))

  return v


def min_value(board):

  if terminal(board):
    return utility(board)

  v = 1
  for action in actions(board):
    v = min(v, max_value(result(board, action)))

  return v
