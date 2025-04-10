import random
def paly():
    user=input("what's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer =random.choice(['r','p','s'])
    if user == computer:
        return 'It's a tie'
    if is_win(user,computer):
        return your won!
        return your lost!
def is_win (player,opponent):
    if(player=='r' and opponent=='s') or (player=='s' and opponent=='p')\
        or(player=='p' and opponent='r'):
        return true
