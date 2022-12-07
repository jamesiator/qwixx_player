from scorecard import ScoreCard, RED, YELLOW, GREEN, BLUE

class Greedy:
  '''
  This player will always make a move if it can.
  If there are more than 1 possible moves, choose one at random.
  '''
  def __init__(self):
    self.scoreCard = ScoreCard()
    self.name = 'greedy'

  def takeTurn(self, dice):
    '''
    The player must make a move; else take a penalty.
    '''

  def makeMove(self, dice):
    '''
    If a move can be made, make it.
    '''
    pass

# player who doesn't skip more than 1 number in any row
class SkipOne:
  '''
  This player will never skip more than 1 number in a row.
  Choices are 'better' than others if they don't skip any.
  If there are multiple 'better' choices, choose one at random.

  If there are no choices that satisfy this player's preferences,
  and it is this player's turn, it will take a penalty.
  '''
  def __init__(self):
    self.scoreCard = ScoreCard()
    self.name = 'skipOne'

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
  def __init__(self):
    self.scoreCard = ScoreCard()
    self.name = 'skipTwo'

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
  def __init__(self):
    self.scoreCard = ScoreCard()
    self.name = 'utilitarian'

  def takeTurn(self, dice):
    pass

  def makeMove(self, dice):
    pass

class SkipTwoOnce:
  '''
  This player will allow itself to skip 2 squares just once during the game.
  Otherwise it will make the best available decision
  '''
  def __init__(self):
    self.scoreCard = ScoreCard()
    self.name = 'skipTwoOnce'

  def takeTurn(self, dice):
    pass

  def makeMove(self, dice):
    pass