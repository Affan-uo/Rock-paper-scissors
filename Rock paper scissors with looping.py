while True :
    import random 
    print('ROCK.....\nPAPER ......\nSCISSORS....')
    options=['rock','paper','scissors']
    player=input('player what do you pick ?  ').lower()
    if player not in options :
         print(f'Please pick from this list{options}')
    computer=(random.choice(options))
    print(f'computer plays {computer}')
#     print('No cheating! \n'*10)
    if player==computer :
       print("IT'S  A TIE  !")
    if computer=='rock' and player=='scissors':
       print('COMPUTER WINS !')
    elif player=='rock' and computer=='scissors':
         print('PLAYER WINS !')
    elif computer=='paper' and player=='rock':
         print('COMPUTER WINS !')
    elif player=='paper' and computer=='rock':
         print('PLAYER WINS !')
    elif computer=='scissors' and player=='paper':
         print('COMPUTER WINS !')
    elif player=='scissors' and computer=='paper':
         print('PLAYER WINS!')
    else:
         print('TRY AGAIN !')
    user=input("TO CONTINUE TYPE 'y',TO STOP TYPE 'n ' !!!  ").lower()
    if user == 'n' :
        break
    elif user == "y" :
        import random