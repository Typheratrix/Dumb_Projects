import random

def play():
    user = input("'r' for rock, 'p' for paper, 's' scissors")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'

    if is_win(user, computer):
        return 'You Won!'

    return 'You lost!'

def is_win(player, opponent):
    #return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player =='p' and opponent == 'r'):
        return True