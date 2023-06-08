'''
Rock Paper Scissors by Timothy Eden
Date Last Updated: May 16, 2023

This program simulates a 2-player game of Rock Paper Scissors. Any number of the 2 players
can either be human or computer-controlled. This game also includes a 1% chance of the results
being completely reversed (i.e. scissors beats rock), and also each computer-controlled player
has a 1% chance of selecting a fourth option, "bomb", which beats rock, paper, and scissors.
'''


import random


def tie_breaker():
    '''
    This is a simple function that decides who wins in a tie. It is only used in
    reverse_rps_winner, as in the normal game, it's just called as a tie.

    :return: This function just generates a random number, 1 or 2, and returns it.
    '''
    x = random.randint(1,2)
    return x


def rps_winner(player1, player2):
    '''
    This function has a 99% chance of being called, and returns the results of the 2
    player's moves as normal.

    :param player1: What player 1 selected

    :param player2: What player 2 selected

    :return: Returns the result, although this is not needed in the final program and was
    just used for testing.
    '''
    if player1 == 'rock':
        if player2 == 'rock':
            print('It\'s a tie!')
            return 'tie'
        elif player2 == 'paper':
            print('Paper beats rock!')
            print('Player 2 wins!')
            return 'player2'
        elif player2 == 'scissors':
            print('Rock beats scissors!')
            print('Player 1 wins!')
            return 'player1'
        elif player2 == 'bomb':
            print('Bomb beats rock!')
            print('Player 2 wins!')
            return 'player2'
    elif player1 == 'paper':
        if player2 == 'rock':
            print('Paper beats rock!')
            print('Player 1 wins!')
            return 'player1'
        elif player2 == 'paper':
            print('It\'s a tie!')
            return 'tie'
        elif player2 == 'scissors':
            print('Scissors beats paper!')
            print('Player 2 wins!')
            return 'player2'
        elif player2 == 'bomb':
            print('Bomb beats paper!')
            print('Player 2 wins!')
            return 'player2'
    elif player1 == 'scissors':
        if player2 == 'rock':
            print('Rock beats scissors!')
            print('Player 2 wins!')
            return 'player2'
        elif player2 == 'paper':
            print('Scissors beats paper!')
            print('Player 1 wins!')
            return 'player1'
        elif player2 == 'scissors':
            print('It\'s a tie!')
            return 'tie'
        elif player2 == 'bomb':
            print('Bomb beats scissors!')
            print('Player 2 wins!')
            return 'player2'
    elif player1 == 'bomb':
        if player2 == 'rock':
            print('Bomb beats rock!')
            print('Player 1 wins!')
            return 'player1'
        elif player2 == 'paper':
            print('Bomb beats paper!')
            print('Player 1 wins!')
            return 'player1'
        elif player2 == 'scissors':
            print('Bomb beats scissors!')
            print('Player 1 wins!')
        elif player2 == 'bomb':
            print('It\'s a tie!')
            return 'tie'


def reverse_rps_winner(player1, player2):
    '''
    This function has a 1% chance of being called, and returns the results
    of the game in reverse. It also allows one randomly selected player to
    win in a tie. Despite the reversed results, bomb still wins against everything.

    :param player1: What player 1 selected

    :param player2: What player 2 selected

    :return: Returns the result, although this is not needed in the final program and was
    just used for testing.
    '''
    if player1 == 'rock':
        if player2 == 'rock':
            print('Rock beats rock!')
            x = tie_breaker()
            if x == 1:
                print('Player 1 wins!')
            elif x == 2:
                print('Player 2 wins!')
        elif player2 == 'paper':
            print('Rock beats paper!')
            print('Player 1 wins!')
            return 'player1'
        elif player2 == 'scissors':
            print('Scissors beats rock!')
            print('Player 2 wins!')
            return 'player2'
        elif player2 == 'bomb':
            print('Bomb beats rock!')
            print('Player 2 wins!')
            return 'player2'
    elif player1 == 'paper':
        if player2 == 'rock':
            print('Rock beats paper!')
            print('Player 2 wins!')
            return 'player2'
        elif player2 == 'paper':
            print('Paper beats paper!')
            x = tie_breaker()
            if x == 1:
                print('Player 1 wins!')
            elif x == 2:
                print('Player 2 wins!')
        elif player2 == 'scissors':
            print('Paper beats scissors!')
            print('Player 1 wins!')
            return 'player1'
        elif player2 == 'bomb':
            print('Bomb beats paper!')
            print('Player 2 wins!')
            return 'player2'
    elif player1 == 'scissors':
        if player2 == 'rock':
            print('Scissors beats rock!')
            print('Player 1 wins!')
            return 'player1'
        elif player2 == 'paper':
            print('Paper beats scissors!')
            print('Player 2 wins!')
            return 'player2'
        elif player2 == 'scissors':
            print('Scissors beats scissors!')
            x = tie_breaker()
            if x == 1:
                print('Player 1 wins!')
            elif x == 2:
                print('Player 2 wins!')
        elif player2 == 'bomb':
            print('Bomb beats scissors!')
            print('Player 2 wins!')
            return 'player2'
    elif player1 == 'bomb':
        if player2 == 'rock':
            print('Bomb beats rock!')
            print('Player 1 wins!')
            return 'player1'
        elif player2 == 'paper':
            print('Bomb beats paper!')
            print('Player 1 wins!')
            return 'player1'
        elif player2 == 'scissors':
            print('Bomb beats scissors!')
            print('Player 1 wins!')
        elif player2 == 'bomb':
            print('It\'s a tie!')
            return 'tie'


def computer_move():
    '''
    This function randomly generates the computer's move. It has a 1% chance of selecting
    "bomb". Otherwise, it will randomly select between "rock", "paper", or "scissors".

    :return: Returns the computer's selection in the form of a string.
    '''
    x = random.randint(1,3)
    b = random.randint(1,100)
    if b == 100:
        return 'bomb'
    else:
        if x == 1:
            return 'rock'
        elif x == 2:
            return 'paper'
        elif x == 3:
            return 'scissors'


def player_move():
    '''
    This function gets the player's move through user input. It only allows 'rock',
    'paper', or 'scissors' as inputs, and otherwise will just print 'Invalid input'
    and ask again. There is no way for a player's move to be set as "bomb" through
    this function.
    :return:
    '''
    while True:
        print('You may select rock, paper, or scissors.')
        x = input('> ')
        if x == 'rock':
            return 'rock'
        elif x == 'paper':
            return 'paper'
        elif x == 'scissors':
            return 'scissors'
        else:
            print('Invalid input.')
            pass



def __main__():
    '''
    This runs the game.
    '''
    print('Welcome to Rock Paper Scissors!')
    while True:
        while True:
            print('How many will play?')
            nop = input('> ')
            if nop == '0' or nop == '1' or nop == '2':
                nop = int(nop)
                break
            else:
                pass
        if nop == 0:
            print('Player 1, please enter your move.')
            player1 = computer_move()
            print('Player 2, please enter your move.')
            player2 = computer_move()
        elif nop == 1:
            print('Player 1, please enter your move.')
            player1 = player_move()
            print('Player 2, please enter your move.')
            player2 = computer_move()
        elif nop == 2:
            print('Player 1, please enter your move.')
            player1 = player_move()
            print('Player 2, please enter your move.')
            player2 = player_move()
        rev = random.randint(1,100)
        if rev == 100:
            reverse_rps_winner(player1, player2)
        else:
            rps_winner(player1, player2)
        print('Play again?')
        if not input('> ').startswith(('y', 'Y')):
            break


__main__()
