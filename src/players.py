from scorecard import ScoreCard

class Greedy:
  '''
  This player will always make a move if it can.
  If there are more than 1 possible moves, choose one at random.
  '''
  def __init__(self):
    self.scoreCard = ScoreCard()

  def takeTurn(self, dice):
    '''
    The player must make a move; else take a penalty.
    '''
    pass

  def makeMove(self, dice):
    '''
    If a move can be made, make it.
    '''
    pass

# player who doesn't skip more than 1 number in any row
class SkipOne:
  '''
  This player will give preference to moves that only skip 1 number.
  If there are multiple choices, choose one at random.
  If there are no choices and it is this player's turn, it will take a penalty
  '''
  def __init__(self):
    self.scoreCard = ScoreCard()

  def takeTurn(self, dice):
    '''
    collect all moves that don't skip more than 1 square and choose randomly from those
    '''
    pass

  def makeMove(self, dice):
    pass

class SkipTwo:
  '''
  This player will give preference to moves that skip no more than 2 numbers.
  If there are multiple choices, choose one at random.
  If there are no choices and it is this player's turn, it will take a penalty
  '''
  def __init__(self):
    self.scoreCard = ScoreCard()

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

  def takeTurn(self, dice):
    pass

  def makeMove(self, dice):
    pass


  # come up with more strategies