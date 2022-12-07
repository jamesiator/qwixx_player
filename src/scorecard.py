#!/usr/bin/python3

RED = 'red'
YELLOW = 'yellow'
GREEN = 'green'
BLUE = 'blue'
COLORS = [RED, YELLOW, GREEN, BLUE]

class ScoreCard:

  def __init__(self):

    self.penalties = 0
    self.scores = {color: 0 for color in COLORS}
    self.rows = {color: set(i for i in range(2,13)) for color in COLORS}

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

    for key in self.scores:
      for i in range(self.scores[key]):
        score += i + 1

    for i in range(self.penalties):
      score -= 5

    return score

  def takePenalty(self):
    '''
    Increment the number of penalties.
    If that number reaches 4, the game is over.
    
    return True if the game is over; else return False
    '''
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
    if number == self.lockNumbers[color]:
      return self.scores[color] > 4

    return number in self.rows[color]

  def markRow(self, color, number):
    '''
    Remove any numbers less than/equal to the marked number from the red row.
    Lock the row if number == 12.

    return True if red was locked; else return False
    '''
    if color == RED or color == YELLOW:
      condition = self.condRedYellow
    else: # BLUE or GREEN
      condition = self.condBlueGreen

    self.scores[color] += 1

    if number == self.lockNumbers[color]:
      self.lockRow(color)
      self.scores[color] += 1
    else:
      new_row = set()
      for i in self.rows[color]:
        if condition(i, number):
          new_row.add(i)
      self.rows[color] = new_row

    return len(self.rows[color]) == 0

  def condRedYellow(self, i, number):
    return i > number

  def condBlueGreen(self, i, number):
    return i < number

  def lockRow(self, color):
    '''
    For locking a row from outside this instance
    '''
    self.rows[color] = set()

if __name__ == "__main__":
  testCard = ScoreCard()
  testCard.markRow(RED,2)
  testCard.markRow(RED,3)
  testCard.markRow(RED,4)
  testCard.markRow(RED,5)
  testCard.markRow(RED,6)
  print(testCard.rows[RED])
  print(testCard.get_total_score())
  testCard.markRow(RED,12)
  print(testCard.rows[RED])
  print(testCard.get_total_score())
  # print(testCard.scores)