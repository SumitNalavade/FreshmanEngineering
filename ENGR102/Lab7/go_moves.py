# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Surya Jasper, Sumit Nalavade, Srikar Velavarthipati, Ronit Dhawan
# Section:      524
# Assignment:   Lab 7 Go Moves
# Date:         12 10 2022

# creating a dictionary to store what character we want to use to represent each piece on the board
PIECES = {
  'empty': '.',
  'white': chr(9675),
  'black': chr(9679),
}

# defining a class to manage the state of our board and print it
class Board:
  # our constructor will take one parameter for size
  def __init__(self, size):
    self.size = size

    # initialize our 2d list with empty characters
    self.mat = [ 
      [PIECES['empty'] for i in range(size)] 
        for j in range(size) 
    ]

    # the game will start with white's turn
    self.turn = 'white'
  
  # defining a function to switch the turn from white to black or from black to white
  def switch_turn(self):
    if self.turn == 'white':
      self.turn = 'black'
    else:
      self.turn = 'white'
  
  # defining a function to place a stone in the board given the row and column
  def place_stone(self, row, col):
    # guard clause in case our row or column is out of bounds (too small or too big)
    if row < 0 or row >= len(self.mat) or col < 0 or col >= len(self.mat[0]):
      return print(f'Please enter positions between 1 and {self.size}')
    
    # guard class in case there is already a stone at that row and column position
    if self.mat[row][col] != PIECES['empty']:
      return print('Cannot place stone as there is already a stone in that location')
    
    # if our row and column values are valid, we update the board (represented by the mat attribute)
    # with the appropriate piece which we can find by indexing our PIECES dictionary
    stone = PIECES[self.turn]
    self.mat[row][col] = stone
  
  # lastly, we define a function to print the state of the board
  def print_board(self):
    for row in self.mat:
      # we can simplify our work using the join function condensing each row to a string
      print(''.join(row))

# instantiate our board with size 9x9
board = Board(9)

# the main loop for our game
while True:
  # at the start of each iteration, we want to print whose turn it is and print the state of the board
  print('--------------------')
  print(f'It is {board.turn}\'s turn')
  board.print_board()
  
  # next, we prompt the player for the row and column position they want to place their stone
  inp = input('Please enter where you wish to place your piece [row column] or stop to end your turn: ')

  # if a player enters stop, we switch the turn so the other player can go next and move onto the next iteration
  if inp.lower() == 'stop':
    board.switch_turn()
    continue
  
  # if the user did not enter stop, we first get the row and column values as integers using the split function
  # and converting each element in the new list by mapping it through the int function
  row, col = list(map(int, inp.split()))

  # lastly, we call our board's place_stone function which includes all our input error handling
  board.place_stone(row-1, col-1)
