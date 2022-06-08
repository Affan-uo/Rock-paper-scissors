#Setting the variables.
player_wins= 0
computer_wins= 0
plays=0
winner=int(input('How many times do you want to play? '))
options=['rock','paper','scissors']
#while (player_wins < winner) and (computer_wins < winner) :
while plays < winner :
    import random 
    plays =+ 1
    print(f'player_wins {player_wins} and computer_wins {computer_wins}')
    print('ROCK.....\nPAPER ......\nSCISSORS....')
    print("You can always quit with 'q' ")
    #Asking for player's input
    player=input('player what do you pick ?  ').lower()
    #Setting the conditions.
    if player not in options :
         print(f'Please pick from this list{options}')
    if  player == "q" :
        break
    elif player_wins==winner or computer_wins ==winner :
        break
    computer=(random.choice(options))
    print(f'computer plays {computer}')
    if player==computer :
       print("IT'S  A TIE  !")
    if computer=='rock' and player=='scissors':
       print('COMPUTER WINS !')
       computer_wins += 1
    elif player=='rock' and computer=='scissors':
         print('PLAYER WINS !')
         player_wins += 1
    elif computer=='paper' and player=='rock':
         print('COMPUTER WINS !')
         computer_wins += 1
    elif player=='paper' and computer=='rock':
         print('PLAYER WINS !')
         player_wins += 1
    elif computer=='scissors' and player=='paper':
         print('COMPUTER WINS !')
         computer_wins += 1
    elif player=='scissors' and computer=='paper':
         print('PLAYER WINS!')
         player_wins += 1
    else:
         print('TRY AGAIN !')
if computer_wins > player_wins :
        print('The computer won !') 
elif player_wins > computer_wins :
        print('PLAYER YOU WON !! ') 
elif player_wins == computer_wins :
        print("IT'S A TIE !")