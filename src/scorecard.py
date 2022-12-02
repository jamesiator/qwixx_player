class ScoreCard:
  def __init__(self):
    self.red_left = set(i for i in range(2,13))
    self.yellow_left = set(i for i in range(2,13))
    self.green_left = set(i for i in range(2,13))
    self.blue_left = set(i for i in range(2,13))

    self.red_score = 0
    self.yellow_score = 0
    self.green_score = 0
    self.blue_score = 0
    self.penalties = 0
    
  def get_total_score(self):
    '''
    Get the score of this board
    '''
    score = 0
    for i in range(self.red_score):
      score += i+1

    for i in range(self.yellow_score):
      score += i+1

    for i in range(self.green_score):
      score += i+1

    for i in range(self.blue_score):
      score += i+1

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

  # RED methods ###############
  def canMarkRed(self, number):
    '''
    Helper method to check if this number is available in the red row.

    If the number is 12, check that 5 numbers in red have already been marked:
      if yes, return true; else return false

    Otherwise, simply return whether the given number is available
    '''
    if number == 12:
      return self.red_score > 4

    return number in self.red_left

  def markRed(self, number):
    '''
    Remove any numbers less than/equal to the marked number from the red row.
    Lock the row if number == 12.

    return True if red was locked; else return False
    '''
    new_red_left = set()
    self.red_score += 1

    if number != 12:
      for i in self.red_left:
        if i > number:
          new_red_left.add(i)

    self.red_left = new_red_left

    return number == 12

  def lockRed(self):
    '''
    For locking the row from outside this instance
    '''
    self.red_left = set()
  #############################

  # YELLOW methods ############
  def canMarkYellow(self, number):
    '''
    Helper method to check if this number is available in the yellow row.

    If the number is 12, check that 5 numbers in yellow have already been marked:
      if yes, return true; else return false

    Otherwise, simply return whether the given number is available
    '''
    if number == 12:
      return self.yellow_score > 4

    return number in self.yellow_left

  def markYellow(self, number):
    '''
    Remove any numbers less than/equal to the marked number from the yellow row.
    Lock the row if number == 12.

    return True if yellow was locked; else return False
    '''
    new_yellow_left = set()
    self.yellow_score += 1

    if number != 12:
      for i in self.yellow_left:
        if i > number:
          new_yellow_left.add(i)

    self.yellow_left = new_yellow_left

    return number == 12

  def lockYellow(self):
    '''
    For locking the row from outside this instance
    '''
    self.yellow_left = set()
  #############################

  # GREEN methods #############
  def canMarkGreen(self, number):
    '''
    Helper method to check if this number is available in the green row.

    If the number is 2, check that 5 numbers in green have already been marked:
      if yes, return true; else return false

    Otherwise, simply return whether the given number is available
    '''
    if number == 2:
      return self.green_score > 4

    return number in self.green_left

  def markGreen(self, number):
    '''
    Remove any numbers greater than/equal to the marked number from the green row.
    Lock the row if number == 2.

    return True if green was locked; else return False
    '''
    new_green_left = set()
    self.green_score += 1

    if number != 2:
      for i in self.green_left:
        if i < number:
          new_green_left.add(i)

    self.green_left = new_green_left

    return number == 2

  def lockGreen(self):
    '''
    For locking the row from outside this instance
    '''
    self.green_left = set()
  #############################

  # BLUE methods ##############
  def canMarkBlue(self, number):
    '''
    Helper method to check if this number is available in the blue row.

    If the number is 2, check that 5 numbers in blue have already been marked:
      if yes, return true; else return false

    Otherwise, simply return whether the given number is available
    '''
    if number == 2:
      return self.blue_score > 4

    return number in self.blue_left

  def markBlue(self, number):
    '''
    Remove any numbers greater than/equal to the marked number from the blue row.
    Lock the row if number == 2.

    return True if blue was locked; else return False
    '''
    new_blue_left = set()
    self.blue_score += 1
    
    if number != 2:
      for i in self.blue_left:
        if i < number:
          new_blue_left.add(i)

    self.blue_left = new_blue_left

    return number == 2

  def lockBlue(self):
    '''
    For locking the row from outside this instance
    '''
    self.blue_left = set()
  #############################

if __name__ == "__main__":
  test = ScoreCard()
  print(test.green_left)