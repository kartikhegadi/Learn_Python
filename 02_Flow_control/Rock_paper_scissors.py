import  random
import sys

print(" ROCK, PAPER, SCISSOR")

# these variables keep  track of the number of wins,losses, and ties
wins=0
losses=0
ties=0

while True :
    print("%s wins,%s LOsses,%s Ties"%(wins,losses,ties))
    while True :
        print("Enter your move: r for rock /t p for paper /t s for cissors /t q for quit the game")
        player_move=input()
        if player_move=='q':
            sys.exit()# Quit the program
        if player_move =='r' or player_move == 's' or player_move == 'p' :
            break # break out the player input loop
        print("type one of r , p, s, pr q")
    #displays what the player chose:
    if player_move == 'r' :
        print("ROCK versus..")
    elif player_move=='p':
        print("PAPER versus..")
    elif player_move == 's':
        print("SCISSOR versus..")

    # displays what the compuer chooses:
    random_number= random.randint(1,3)
    if random_number== '1':
        computer_move=' r'
        print("ROCK")
    elif random_number ==2:
        computer_move='p'
        print("PAPER")
    elif random_number =='3':
        computer_move='s'
        print("SCISSORS")

    #displays and record the win/loss/tie
    if player_move==computer_move:
        print("it's tie !!")
        ties+=1
    elif player_move =='r' and computer_move == 's':
        print("you win!")
        wins+=1
    elif player_move == 'p' and computer_move == 'r':
        print("You win!!")
        wins=wins+1
    elif player_move=='s' and computer_move=='p' :
        print("You win!!")
        wins+=1
    elif player_move =='r' and computer_move == 'p' :
        print("You lose!!")
        losses=losses+1
    elif player_move=='p' and computer_move=='s':
        print("You loose!!")
        losses=losses+1
    elif player_move == 's' and computer_move =='r':
        print("You loose!!")
        losses=losses+1

