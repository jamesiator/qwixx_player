from scorecard import ScoreCard, RED, YELLOW, GREEN, BLUE, COLORS
import random

WHITE1 = 'white1'
WHITE2 = 'white2'
GAME_OVER = 'game over'

class Greedy:
  '''
  This player will always make a move if it can.
  If there are more than 1 possible moves, choose one at random.
  '''
  def __init__(self, name):
    self.scoreCard = ScoreCard()
    self.name = name

  def takeTurn(self, dice):
    '''
    This method is called when it is this player's turn.
    The player must make a move; else take a penalty.

    Return a list of colors whose rows were locked, if any;
    else return 'game over' if the player took its final penalty;
    else return None
    '''
    no_move_made = 0
    locked_rows = []

    # get sum of white
    whiteSum = dice[WHITE1] + dice[WHITE2]
    
    # get possible moves w/ white value
    possibleMoves = []
    for die in dice:
      if self.scoreCard.canMarkRow(die, whiteSum):
        possibleMoves.append(die)

    # if there are available moves, choose one at random
    if len(possibleMoves) != 0:
      moveIndex = random.randint(0, len(possibleMoves)-1)
      result = self.scoreCard.markRow(possibleMoves[moveIndex], whiteSum)
      if result is not None: # did we just lock a row? store the color if so
        locked_rows.append(result)
    
    else: # else if there are no available moves, make note.
      no_move_made += 1

    # now attempt to make a move with 
    # a non-white + white dice combo
    
    # get possible moves
    possibleMoves = []
    for die in dice:
      move1 = dice[WHITE1] + dice[die]
      move2 = dice[WHITE2] + dice[die]
      
      if self.scoreCard.canMarkRow(die, move1):
        possibleMoves.append((die, move1)) # store the (color, #) pair
      if self.scoreCard.canMarkRow(die, move2):
        possibleMoves.append((die, move2)) # store the (color, #) pair

    # if there are moves available, make one at random
    if len(possibleMoves) != 0:
      moveIndex = random.randint(0, len(possibleMoves)-1)
      color, number = possibleMoves[moveIndex]
      result = self.scoreCard.markRow(color, number)
      if result is not None: # did we just lock a row? store the color if so
        locked_rows.append(result)
    
    else: # else make note that no move could be made
      no_move_made += 1

    # check if we made a move or need to take a penalty
    if no_move_made == 2:
      if self.scoreCard.takePenalty(): # returns true if we just took our 4th penalty
        return GAME_OVER
    # check if we locked any rows
    elif len(locked_rows) != 0:
      return locked_rows

    # else return nothing

  def makeMove(self, dice):
    '''
    This method is called when it is not this player's turn.
    If a move can be made, make it.

    Return a color if its row was locked;
    else return None
    '''
    # get sum of white
    whiteSum = dice[WHITE1] + dice[WHITE2]

    # get possible moves
    possibleMoves = []
    for die in dice:
      if self.scoreCard.canMarkRow(die, whiteSum):
        possibleMoves.append(die)

    # if there are available moves, choose one at random
    if len(possibleMoves) != 0:
      moveIndex = random.randint(0, len(possibleMoves)-1)
      return self.scoreCard.markRow(possibleMoves[moveIndex], whiteSum)

class SkipOne:
  '''
  This player will never skip more than 1 number in a row.
  Choices are 'better' than others if they don't skip any.
  If there are multiple 'better' choices, choose one at random.

  If there are no choices that satisfy this player's preferences,
  and it is this player's turn, it will take a penalty.
  '''
  def __init__(self, name):
    self.scoreCard = ScoreCard()
    self.name = name

  def takeTurn(self, dice):
    '''
    collect all moves that don't skip more than 1 square and choose randomly from those
    '''
    pass

  def makeMove(self, dice):
    pass

class SkipTwo:
  '''
  This player will never skip more than 2 number in a row.
  If there are multiple best choices, choose one at random.
  If there are no choices and it is this player's turn, it will take a penalty
  '''
  def __init__(self, name):
    self.scoreCard = ScoreCard()
    self.name = name

  def takeTurn(self, dice):
    pass

  def makeMove(self, dice):
    pass

class Utilitarian:
  '''
  This player will use a heuristic to make decisions.

  Choose the options with the most immediate utility.
  Weigh the gains/losses of each possible choice.
  If taking a penalty (-5) is deemed less costly than losing out on numbers by making some move,
  take the penalty.

  If taking a penalty would cause this player to lose, make the next-best move according to utility
  '''
  def __init__(self, name):
    self.scoreCard = ScoreCard()
    self.name = name

  def takeTurn(self, dice):
    pass

  def makeMove(self, dice):
    pass

class SkipTwoOnce:
  '''
  This player will allow itself to skip 2 squares just once during the game.
  Otherwise it will make the best available decision
  '''
  def __init__(self, name):
    self.scoreCard = ScoreCard()
    self.name = name

  def takeTurn(self, dice):
    pass

  def makeMove(self, dice):
    pass