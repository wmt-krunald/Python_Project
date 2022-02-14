import random

def play_rsp():
    user = input("\nWhat is your Choice ?\n 'r' for Rock,\n 's' for Scissors,\n 'p' for Paper\n")
    comp = random.choice(['r','s','p'])
    print("Computer choice: ", comp)


    if user == comp:
        return "It's tie."
    
    if is_win(user, comp):
        return "\nHurreeyyy, You Win this Match."
    else:
        return "\nBetter Luck For Next Time.."
        
#when user win : if -> r > s, s > p, p > r.
def is_win(player, computer):   #This function return True if player will win.
    if (player == 'r' and computer == 's') or (player == 's' and computer == 'p') or (player == 'p' and computer == 'r'):
        return True

print(play_rsp())
