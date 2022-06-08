#Rock paper scissors game
playables=['rock','paper','scissors']
print('ROCK.....\nPAPER ......\nSCISSORS....')
#Asking for inputs

player1=input('player1 what do you pick ?  ')
if player1 not in playables  :
    print(f'please pick one from this list {playables}')
player2=input('player2 what do you pick ?  ')
if player2 not in playables  :
    print(f'please pick one from this list {playables}') 
 #Setting the conditions      
elif player2==player1 :
    print("IT'S  A TIE  !")
elif player1=='rock' and player2=='scissors':
    print('PLAYER1 WINS !')
elif player2=='rock' and player1=='scissors':
     print('PLAYER2 WINS !')
elif player1=='paper' and player2=='rock':
       print('PLAYER1 WINS !')
elif player2=='paper' and player1=='rock':
         print('PLAYER2 WINS !')
elif player1=='scissors' and player2=='paper':
       print('PLAYER1 WINS !')
elif player2=='scissors' and player1=='paper':
         print('PLAYER2 WINS!')
elif player2==player1 :
    print("IT'S  A TIE  !")
#print('congratulations !!!')
else:
     print('TRY AGAIN !')