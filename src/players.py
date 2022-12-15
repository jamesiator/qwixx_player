from scorecard import ScoreCard, RED, YELLOW, GREEN, BLUE, COLORS
import random

WHITE1 = 'white1'
WHITE2 = 'white2'
GAME_OVER = 'game over'

def get_possible_moves(scoreCard: ScoreCard, dice, colors=False):
  '''
  Helper function for getting possible moves from a given scorecard and dice roll.

  Set colors to True if moves from white/nonwhite combos are desired;
  else omit or set to False to get white dice moves.
  '''
  possibleMoves = []

  if colors:
    for color in dice:
      move1 = dice[WHITE1] + dice[color]
      move2 = dice[WHITE2] + dice[color]

      if scoreCard.canMarkRow(color, move1):
        possibleMoves.append((color, move1))
      if scoreCard.canMarkRow(color, move2):
        possibleMoves.append((color, move2))
  else:
    whiteSum = dice[WHITE1] + dice[WHITE2]

    for color in dice:
      if scoreCard.canMarkRow(color, whiteSum):
        possibleMoves.append(color)

  return possibleMoves

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
    possibleMoves = get_possible_moves(self.scoreCard, dice)

    # if there are available moves, choose one at random
    if len(possibleMoves) != 0:
      moveIndex = random.randint(0, len(possibleMoves)-1)
      print(f'{self.name} marks {whiteSum} in {possibleMoves[moveIndex]}')
      result = self.scoreCard.markRow(possibleMoves[moveIndex], whiteSum)
      if result is not None: # did we just lock a row? store the color if so
        locked_rows.append(result)
    
    else: # else if there are no available moves, make note.
      no_move_made += 1

    # now attempt to make a move with 
    # a non-white + white dice combo
    
    # get possible moves
    possibleMoves = get_possible_moves(self.scoreCard, dice, colors=True)

    # if there are moves available, make one at random
    if len(possibleMoves) != 0:
      moveIndex = random.randint(0, len(possibleMoves)-1)
      color, number = possibleMoves[moveIndex]
      print(f'{self.name} marks {number} in {color}')
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
    possibleMoves = get_possible_moves(self.scoreCard, dice)

    # if there are available moves, choose one at random
    if len(possibleMoves) != 0:
      moveIndex = random.randint(0, len(possibleMoves)-1)
      print(f'{self.name} marks {whiteSum} in {possibleMoves[moveIndex]}')
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
    collect all valid moves, prioritizing moves that don't skip more than 1,
    and choose randomly from those
    '''
    no_move_made = 0
    locked_rows = []

    # get sum of white
    whiteSum = dice[WHITE1] + dice[WHITE2]
    
    # get possible moves w/ white value
    possibleMoves = get_possible_moves(self.scoreCard, dice)

    # prioritize:
    # if a move skips more than 1, discard it
    # store options that skip 1 or 0
    validMoves = {
      'none': [],
      'one': []
    }
    for move in possibleMoves:
      if move == RED or move == YELLOW:
        if whiteSum-1 not in self.scoreCard.rows[move]:
          validMoves['none'].append(move)
        elif whiteSum-2 not in self.scoreCard.rows[move]:
          validMoves['one'].append(move)
      else: # green or blue
        if whiteSum+1 not in self.scoreCard.rows[move]:
          validMoves['none'].append(move)
        elif whiteSum+2 not in self.scoreCard.rows[move]:
          validMoves['one'].append(move)

    # if there are options that don't skip any numbers, choose from there
    if len(validMoves['none']) != 0:
      idx = random.randint(0,len(validMoves['none'])-1)
      print(f'{self.name} marks {whiteSum} in {validMoves["none"][idx]}')
      result = self.scoreCard.markRow(validMoves['none'][idx], whiteSum)
      if result is not None: # did we just lock a row? store if so
        locked_rows.append(result)
    # else if there are options that only skip 1, choose from there
    elif len(validMoves['one']) != 0:
      idx = random.randint(0, len(validMoves['one'])-1)
      print(f'{self.name} marks {whiteSum} in {validMoves["one"][idx]}')
      result = self.scoreCard.markRow(validMoves['one'][idx], whiteSum)
      if result is not None: # did we just lock a row?
        locked_rows.append(result)
    # else, we won't make a move
    else:
      no_move_made += 1

    # now attempt to make a move with a white/non-white combo
    # get possible moves
    possibleMoves = get_possible_moves(self.scoreCard, dice, colors=True)

    # prioritize:
    # if a move skips more than 1, discard it
    # store options that skip 1 or 0
    validMoves = {
      'none': [],
      'one': []
    }
    for color, number in possibleMoves:
      if color == RED or color == YELLOW:
        if number-1 not in self.scoreCard.rows[color]:
          validMoves['none'].append((color,number))
        elif number-2 not in self.scoreCard.rows[color]:
          validMoves['one'].append((color,number))
      else: # green or blue
        if number+1 not in self.scoreCard.rows[color]:
          validMoves['none'].append((color,number))
        elif number+2 not in self.scoreCard.rows[color]:
          validMoves['one'].append((color,number))

    # if there are options that don't skip a number, choose one at random
    if len(validMoves['none']) != 0:
      idx = random.randint(0, len(validMoves['none'])-1)
      color, number = validMoves['none'][idx]
      print(f'{self.name} marks {number} in {color}')
      result = self.scoreCard.markRow(color, number)
      if result is not None: # did we just lock a row?
        locked_rows.append(result)
    # else if there are options that only skip one number, choose one at random
    elif len(validMoves['one']) != 0:
      idx = random.randint(0, len(validMoves['one'])-1)
      color, number = validMoves['one'][idx]
      print(f'{self.name} marks {number} in {color}')
      result = self.scoreCard.markRow(color, number)
      if result is not None: # did we just lock a row?
        locked_rows.append(result)
    # else, we don't make a move
    else:
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
    If a move can be made that skips no more than 1 square, make it.

    Return a color if its row was locked;
    else return None
    '''
    # get sum of white
    whiteSum = dice[WHITE1] + dice[WHITE2]
    
    # get possible moves w/ white value
    possibleMoves = get_possible_moves(self.scoreCard, dice)

    # prioritize:
    # if a move skips more than 1, discard it
    # store options that skip 1 or 0
    validMoves = {
      'none': [],
      'one': []
    }
    for move in possibleMoves:
      if move == RED or move == YELLOW:
        if whiteSum-1 not in self.scoreCard.rows[move]:
          validMoves['none'].append(move)
        elif whiteSum-2 not in self.scoreCard.rows[move]:
          validMoves['one'].append(move)
      else: # green or blue
        if whiteSum+1 not in self.scoreCard.rows[move]:
          validMoves['none'].append(move)
        elif whiteSum+2 not in self.scoreCard.rows[move]:
          validMoves['one'].append(move)

    # if there are options that don't skip any numbers, choose from there
    if len(validMoves['none']) != 0:
      idx = random.randint(0,len(validMoves['none'])-1)
      print(f'{self.name} marks {whiteSum} in {validMoves["none"][idx]}')
      return self.scoreCard.markRow(validMoves['none'][idx], whiteSum)
    # else if there are options that only skip 1, choose from there
    elif len(validMoves['one']) != 0:
      idx = random.randint(0, len(validMoves['one'])-1)
      print(f'{self.name} marks {whiteSum} in {validMoves["one"][idx]}')
      return self.scoreCard.markRow(validMoves['one'][idx], whiteSum)

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