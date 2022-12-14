#!/usr/bin/python3.8

from players import *
from scorecard import *
import sys

WHITE1 = 'white1'
WHITE2 = 'white2'
GAME_OVER = 'game over'

# validate user input
if len(sys.argv) < 3 or len(sys.argv) > 6:
  print('''Please enter between 2 and 5 players (inclusive)
    Available options:
    - greedy
    - skipOne
    - skipTwo
    - utilitarian
    - skipTwoOnce''')
  exit()

# get players
players = []
for i in range(1,len(sys.argv)):
  playerType = str(sys.argv[i]).lower()
  if playerType == 'greedy':
    players.append(Greedy(f'{playerType}{i}'))
  elif playerType == 'skipone':
    players.append(SkipOne(f'{playerType}{i}'))
  elif playerType == 'skiptwo':
    players.append(SkipTwo(f'{playerType}{i}'))
  elif playerType == 'utilitarian':
    players.append(Utilitarian(f'{playerType}{i}'))
  elif playerType == 'skiptwoonce':
    players.append(SkipTwoOnce(f'{playerType}{i}'))

# validate players
if len(players) < 2:
  print('unknown error')
  exit()

# set up the game
dice = {
  WHITE1: 0,
  WHITE2: 0,
  RED: 0,
  YELLOW: 0,
  GREEN: 0,
  BLUE: 0
}
game_over = False

# run the game
while not game_over:
  for i in range(len(players)):
    # get the player whose turn it is
    currentPlayer = players[i]
    lockedColors = set()

    # roll the dice
    for die in dice:
      dice[die] = random.randint(1,6)

    # current player takes turn
    currentPlayerResult = currentPlayer.takeTurn(dice)
    # if the player took its 4th penalty, no futher turns will be taken
    if currentPlayerResult == GAME_OVER:
      game_over = True
    # if the current player locked a row, store it
    elif currentPlayerResult in COLORS:
      lockedColors.add(currentPlayerResult)

    # rest of players optionally play
    for j in range(len(players)):
      if j != i:
        result = players[j].makeMove(dice)
        # if a player locked a row, store which color got locked
        if result in COLORS:
          lockedColors.add(result)

    # if a color was locked, remove its die and 
    # mark its row as locked on each player's scorecard
    for color in lockedColors:
      # if color in dice:
      del dice[color]
      for player in players:
        player.scoreCard.lockRow(color)

    # check if game is over due to 2 or more rows being locked
    if len(dice) < 5:
      game_over = True

# now get players' scores and show final scorecards
topScore = 0
winner = ''
for player in players:
  print(f"{player.name}'s scorecard:")
  player.scoreCard.printCard()

  score = player.scoreCard.get_total_score()
  print(f'Score = {score}')

  print('--------------------------------')

  if score > topScore:
    topScore = score
    winner = player.name

print(f'{winner} wins!')