#!/usr/bin/python3

from colorama import Fore

RED = 'red'
YELLOW = 'yellow'
GREEN = 'green'
BLUE = 'blue'
COLORS = set((RED, YELLOW, GREEN, BLUE))

class ScoreCard:

  def __init__(self):

    self.penalties = 0
    self.scores = {color: 0 for color in COLORS}
    self.rows = {color: set(i for i in range(2,13)) for color in COLORS}
    self.marked = {color: set() for color in COLORS}

    self.lockNumbers = {
      RED: 12,
      YELLOW: 12,
      GREEN: 2,
      BLUE: 2
    }

  def get_total_score(self):
    '''
    Get the score of this board
    '''
    score = 0

    for color in self.scores:
      score += self.get_score(color)

    for i in range(self.penalties):
      score -= 5

    return score

  def get_score(self, color):
    '''
    Get score of a specific row
    '''
    score = 0
    for i in range(self.scores[color]):
      score += i + 1
    return score

  def get_utility(self, color):
    '''
    Get the value of marking an additional number in a specific row
    '''
    score = 0
    for i in range(self.scores[color]+1):
      score += i + 1
    return score - self.get_score(color)

  def takePenalty(self):
    '''
    Increment the number of penalties.
    If that number reaches 4, the game is over.
    
    return True if the game is over; else return False
    '''
    print('penalty taken')
    self.penalties += 1
    return self.penalties == 4

  def rowsAvailable(self, number):
    '''
    Return rows available to fill out
    '''
    options = []

    for color in COLORS:
      if self.canMarkRow(color,number):
        options.append(color)

    return options

  def canMarkRow(self, color, number):
    '''
    Helper method to check if this number is available in the given color's row.

    If the number is a locking number, check that 5 numbers in the row have already been marked:
      if yes, return true; else return false

    Otherwise, simply return whether the given number is available
    '''
    if color not in COLORS:
      return False

    if number == self.lockNumbers[color]:
      return self.scores[color] > 4

    return number in self.rows[color]

  def markRow(self, color, number):
    '''
    Remove any numbers less than/equal to the marked number from <color>'s row.
    Lock <color>'s row if the number is its locking number.

    return <color> if <color>'s row was locked; else return None
    '''
    if color == RED or color == YELLOW:
      condition = self.condRedYellow
    else: # BLUE or GREEN
      condition = self.condBlueGreen

    self.scores[color] += 1
    self.marked[color].add(number)

    if number == self.lockNumbers[color]:
      self.lockRow(color)
      self.scores[color] += 1
      self.marked[color].add('$')
    else:
      new_row = set()
      for i in self.rows[color]:
        if condition(i, number):
          new_row.add(i)
      self.rows[color] = new_row

    if len(self.rows[color]) == 0:
      return color

  def condRedYellow(self, i, number):
    return i > number

  def condBlueGreen(self, i, number):
    return i < number

  def lockRow(self, color):
    '''
    For locking a row from outside this instance
    '''
    self.rows[color] = set()

  def printCard(self):
    '''
    For displaying board in its current state
    '''
    scorecardRows = {
      RED: '',
      YELLOW: '',
      GREEN: '',
      BLUE: ''
    }
    for color in COLORS:

      if color == RED or color == YELLOW:
        for i in range(2,13):
          if i in self.marked[color]:
            scorecardRows[color] += 'x '
          else:
            scorecardRows[color] += f'{i} '
      else: # printing green and blue rows
        for i in range(12,1,-1):
          if i in self.marked[color]:
            scorecardRows[color] += 'x '
          else:
            scorecardRows[color] += f'{i} '

      # '$' indicates the bonus slot marked 
      # if this player locked this row
      if '$' in self.marked[color]:
        scorecardRows[color] += 'x'
      else:
        scorecardRows[color] += '$'

    penalties = 'Penalties: '
    for i in range(self.penalties):
      penalties += 'x '
    print(Fore.RED + scorecardRows[RED])
    print(Fore.YELLOW + scorecardRows[YELLOW])
    print(Fore.GREEN + scorecardRows[GREEN])
    print(Fore.BLUE + scorecardRows[BLUE])
    print(Fore.WHITE + penalties)

if __name__ == "__main__":
  testCard = ScoreCard()
  testCard.markRow(RED,2)
  testCard.markRow(RED,3)
  testCard.markRow(RED,4)
  testCard.markRow(RED,5)
  testCard.markRow(RED,7)
  # print(testCard.rows[RED])
  # print(testCard.get_total_score())
  testCard.markRow(RED,12)
  # print(testCard.rows[RED])
  # print(testCard.get_total_score())
  # print(testCard.scores)
  testCard.printCard()