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
    players.append(Greedy())
  elif playerType == 'skipone':
    players.append(SkipOne())
  elif playerType == 'skiptwo':
    players.append(SkipTwo())
  elif playerType == 'utilitarian':
    players.append(Utilitarian())
  elif playerType == 'skiptwoonce':
    players.append(SkipTwoOnce())

# validate players
if len(players) < 2:
  print('unknown error')
  exit()

# start the game
dice = {
  WHITE1: 0,
  WHITE2: 0,
  RED: 0,
  YELLOW: 0,
  GREEN: 0,
  BLUE: 0
}

game_over = False
num_locked_rows = 0

while not game_over:
  for i in range(len(players)):
    # player who's turn it is
    currentPlayer = players[i]

    # roll dice
    for die in dice:
      dice[die] = random.randint(1,6)

    # current player takes turn or penalty

    # rest of players optionally play

    # check if game is over
    if len(dice) < 5:
      game_over = True

# now get players' scores and show final standings
topScore = 0
winner = ''
for player in players:
  print(f"{player.name}'s scorecard:")
  player.scoreCard.printBoard()
  score = player.scoreCard.get_total_score()
  print(f'Score = {score}')
  if score > topScore:
    topScore = score
    winner = player.name

print(f'{winner} wins!')