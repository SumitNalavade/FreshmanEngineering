# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Surya Jasper, Sumit Nalavade, Ronit Dhawan, Srikar Velavarthipati
# Section:      524
# Assignment:   Lab 13 Fun Game
# Date:         28 November 2022

import os
import turtle as t

def gen_arr(shape, val=0):
  '''Recursive function to generate n-dimensional python list of a given shape

  Arguments:
  shape -- a list specifying the number of dimensions and the size of each dimension
  '''

  # base case to append number / string to list in last dimension
  if len(shape) == 0:
    return val
  
  # create subarrays using recursive calls and append them to a return array
  ret_arr = []
  for _ in range(shape[0]):
    sub_arr = gen_arr(shape[1:], val=val)
    ret_arr.append(sub_arr)
  
  # return return array
  return ret_arr

# list to convert integer color ids to color strings
COLORS = ['white', 'red', 'yellow']
PADDING = 6

class Connect4Board():
  def __init__(self, NUM_ROWS, NUM_COLS):
    self.xmax = NUM_COLS
    self.ymax = NUM_ROWS

    # calculate radius of circles (involved in later turtle drawing calculations)
    self.radius = 1000 / NUM_COLS / 2

    # initialize board given number of rows and number of columns
    self.board = gen_arr([NUM_COLS, NUM_ROWS])

    # start game with red's turn
    self.turn = 1

  def switch_turn(self):
    # switch turn between red and yellow
    self.turn = 1 if self.turn == 2 else 2
  
  def place_piece(self, x):
    '''Place current player's piece in specified column

    Arguments:
    x -- the index of the column to place the player's piece

    Return:
    False if the column is already filled
    True if the column has open slots and the piece was successfully placed
    '''
    for y in range(len(self.board[x])):
      if self.board[x][y] == 0:
        self.board[x][y] = self.turn
        self.fill_piece(x, y, self.turn)
        return True
    return False
  
  def check_dir(self, x, y, dx, dy):
    '''Check a given row, column, or diagonal for a win condition

    Arguments:
    x  -- the x index of the board to start with (column)
    y  -- the y index of the board to start with (row)
    dx -- direction of search in x axis (delta x) 
    dy -- direction of search in y axis (delta y) 

    Return:
    0 if no win condition is met in this direction
    1 if red won
    2 if yellow won
    '''

    piece = 1
    streak = 0

    # search in the direction until a win condition is met or we go out of bounds
    while streak < 4 and x >= 0 and x < self.xmax and y >= 0 and y < self.ymax:
      # increment the streak if we found the same piece in the next position
      if self.board[x][y] == piece:
        streak += 1
      # otherwise, we set the new piece we found to the piece to search for and reset our streak to 1
      else:
        piece = self.board[x][y]
        streak = 1
      
      # increment x and y by delta x and delta y to continue our search
      x += dx
      y += dy
    
    # return the winning color id if a win condition is met, otherwise return 0 
    return piece if streak == 4 else 0

  def check_win(self):
    '''Check if a win / draw condition has been met
    Checks vertically, horizontally, and diagonally

    Return:
    0 if no win condition was met
    1 if red won
    2 if yellow won
    3 if it was a draw (every slot has been filled)
    '''

    # initialize winner return to no winner
    winner = 0

    # check vertical
    for x in range(self.xmax):
      winner = winner or self.check_dir(x, 0, 0, 1)
    
    # check horizontal
    for y in range(self.ymax):
      winner = winner or self.check_dir(0, y, 1, 0)
    
    # diagonals
    for x in range(3, self.xmax):
      winner = winner or self.check_dir(x, 0, -1, 1)
    
    for x in range(0, self.xmax-3):
      winner = winner or self.check_dir(x, 0, 1, 1)
    
    for y in range(3, self.ymax):
      winner = winner or self.check_dir(0, y, 1, -1)
    
    for y in range(0, self.ymax-3):
      winner = winner or self.check_dir(0, y, 1, 1)
    
    # check for draw
    draw = True
    for col in self.board:
      for val in col:
        if val == 0:
          draw = False
    if draw:
      winner = 3
    
    # return winner (0 means no win condition has been met)
    return winner
  
  def save(self):
    # save our current board configuration and current turn into a file 
    with open('board.txt', 'w') as bout:
      bout.write(str(self.turn) + '\n')
      for row in self.board:
        bout.write(''.join(list(map(str, row))) + '\n')
  
  def load(self):
    '''Load saved game if one exists
    Set up board configuration and turn based on save file

    Return:
    False if there is no saved game
    True if a saved game was found and successfully loaded
    '''

    if not os.path.exists('board.txt'):
      return False
  
    with open('board.txt', 'r') as bout:
      lines = bout.readlines()

      self.turn = int(lines[0])

      for x, row in enumerate(lines[1:]):
        for y, piece in enumerate(row.strip()):
          self.board[x][y] = int(piece)
    
    return True
  
  def game_to_world(self, xgame, ygame):
    '''Convert game coordinates (column, row) to turtle window world coordinates
    
    Arguments:
    xgame -- column index
    ygame -- row index

    Return:
    xworld -- world x coordinate
    yworld -- world y coordinate
    '''

    xworld = xgame / self.xmax * 1000 + self.radius
    yworld = ygame / self.ymax * 1000

    return xworld, yworld
  
  def fill_piece(self, xgame, ygame, piece):
    '''Fill piece in game window with corresponding piece color
    
    Arguments:
    xgame -- column index
    ygame -- row index
    piece -- color id of piece to be placed
    '''
    
    # set speed and delay to 0 so drawing happens instantly
    t.speed(0)
    t.delay(0)

    x, y = self.game_to_world(xgame, ygame)
    color = COLORS[piece]

    t.penup()
    t.setposition(x, y)

    t.fillcolor(color)
    t.pendown()
    t.begin_fill()
    t.circle(self.radius - PADDING)
    t.end_fill()

  def draw(self):
    # set background to blue like standard connect 4 board
    t.clearscreen()
    t.bgcolor('blue')

    # draw current board configuration (empty slots are filled in white)
    for xgame, col in enumerate(self.board):
      for ygame, val in enumerate(col):
        self.fill_piece(xgame, ygame, val)

def init_turtle(w_width, w_height):
  # initialize window and set origin to bottom left instead of screen center
  t.screensize(w_width, w_height)
  t.setworldcoordinates(0, 0, 1000, 1000)

def print_rules():
  # print the rules of the game
  print()
  print(f'-------------------------------------------RULES-------------------------------------------')
  print('In Connect 4, your objective is to place your pieces in the board to achieve a 4 in a row. ')
  print('You can achieve a connect 4 horizontally, vertically, or diagonally. ')
  print('You will play against 1 opponent and compete to get your connect 4 before they beat you to it.')
  print('On a given turn, you may choose to place a piece, read the rules, or end the game.')
  print('Good luck, and have fun!!')
  print('--------------------------------------------------------------------------------------------')
  print()

if __name__ == '__main__':
  # initialize turtle window
  sizex, sizey = 7, 6
  init_turtle(700, 600)

  # initialize connect 4 board object and draw its starting configuration
  board = Connect4Board(sizey, sizex)
  if board.load():
    print('Loaded saved game')
  board.draw()

  # store whether or not the game was exited before a win / draw condition was met 
  game_exited = False

  num_moves = 0
  winner = 0

  print_rules()

  # main loop of game (keeps executing as long as a win condition hasn't been met)
  while not winner:
    print(f'------------------------------------------MOVE {num_moves+1}------------------------------------------')
    # print current player's turn
    print(f'It is {COLORS[board.turn]}\'s turn!')

    pos = -1
    # execute until a valid input has been entered
    while pos <= 0 or pos > sizex:
      # get raw string input
      res = input(f'You can select a column between 1 and {sizex}, enter STOP to save and play later, or enter RULES to read the rules: ')

      # if user entered STOP, save the game and exit
      if res.upper() == 'STOP':
        board.save()
        game_exited = True
        break

      # if the user entered RULES, print rules        
      elif res.upper() == 'RULES':
        print_rules()

      # otherwise, we check if a valid number was inputted for the position to place a piece in
      else:
        try:
          # here, we try converting the user's input to an integer
          pos = int(res)

          # make sure the position entered was within bounds
          if pos <= 0 or pos > sizex:
            print('You selected a column that\'s out of range. Please try again.')
            continue
          
          # place the piece in the inputted position
          place_success = board.place_piece(pos-1)

          # prompt the user on whether or not their piece could be successfully placed in their inputted column
          if place_success:
            print(f'Successfully placed {COLORS[board.turn]} piece in column {pos}!')
          else:
            # if the column was full, reset the position to -1 so the input loop continues
            print(f'Column {pos} is full. Please choose another column.')
            pos = -1

        except ValueError:
          # prompt the user to enter an integer if we received something else
          print(f'Please enter an integer value, STOP, or RULES')
    
    # break out of the main game loop if the user had entered STOP
    if game_exited:
      break
    
    # otherwise, we switch the turn to the next player
    board.switch_turn()

    # increment the number of moves by 1 and check if we have a winner / draw
    num_moves += 1
    winner = board.check_win()

    print('-----------------------------------------------------------------------------------------')
    print()
  
  # if the game exited, prompt the user that their save was successful
  if game_exited:
    print('Game successfully saved and exited! Click on turtle window to close.')
  else:
    # otherwise, since the game is complete, we remove our save file so the next game starts from scratch
    if os.path.exists('board.txt'):
      os.remove('board.txt')
    # print whether the game ended in a draw or if someone won
    if winner == 3:
      print('The game ended in a draw!')
    else:
      print(f'{COLORS[winner]} won in {num_moves} moves!!!')

  # close the turtle window
  t.exitonclick()