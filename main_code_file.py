########## Project_1: Snake,Water,Gun Game ##########################

('''
-1 : snake
0 : water
1 : gun''')

'''concept of the game:
   snake can beat water by drinking and finishing it
   water can beat gun as gun will be malfunctioned if attacked by water
   gun can beat snake as snake will die if shot by the gun'''

import random                          
next_chance='yes'
Hi_score=0

while (next_chance=='yes'):             #Loop for repetition of game.


    computer = random.choice([0, 1, -1])          # computer is choosing one of the options randomly

    dict={'s':-1,'w':0,'g':1}
    reverse_dict={-1:'snake',0:'water',1:'gun'}

    user_input=input('Enter \'s\' for snake,\'w\' for water,\'g\' for gun :') # Taking user's choice
    user_num=dict[user_input]
    computer_choice=reverse_dict[computer]

    print(f'Your choice : {user_input}')
    print(f'Computer choice : {computer_choice}')

    # Code to decide outcome of the game

    if (computer==user_num):
        print('This is a draw.')
    else:
        if (computer==-1 and user_num==1):
            print('You win.Computer lose.')
        elif (computer==-1 and user_num==0):
            print('You lose.Computer win.')
        elif (computer==0 and user_num==-1):
            print('You win.Computer lose.')
        elif (computer==0 and user_num==1):
            print('You lose.Computer win.')
        elif (computer==1 and user_num==-1):
            print('You lose.Computer win.')
        elif (computer==1 and user_num==0):
            print('You win.Computer lose.')
        else:
            print('An error occured.')
            
    # Asking user for a next chance
    
    next_chance=input('Enter yes if want to play again :')
    
    # Program to store high score in file: Hi_score
    
    # condition to win
    cond_win=(computer==-1 and user_num==1) or (computer==0 and user_num==-1) or (computer==1 and user_num==0)
    
    # condition to lose
    cond_lose= (computer==-1 and user_num==0) or (computer==0 and user_num==1) or (computer==1 and user_num==-1)
    
    if (next_chance=='yes'):
        if (cond_win):
            Hi_score+=1
        if(cond_lose):
            with open('Hi_score.txt') as file:
                prev_Hi_score=file.read()
                if (prev_Hi_score==''):
                    with open('Hi_score.txt','w') as file:
                        file.write(str(Hi_score))
                elif ((int(prev_Hi_score))<(Hi_score)):
                    print('previous high score :',prev_Hi_score)
                    print('current high score :',Hi_score)
                    with open('Hi_score.txt','w') as file:
                        file.write(str(Hi_score))        
            Hi_score=0
            
    else:
        if (cond_win):
            Hi_score+=1
        with open('Hi_score.txt') as file:
            prev_Hi_score=file.read()
            if (prev_Hi_score==''):
                with open('Hi_score.txt','w') as file:
                        file.write(str(Hi_score))
            elif ((int(prev_Hi_score))<(Hi_score)):
                print('previous high score :',prev_Hi_score)
                print('current high score :',Hi_score)
                with open('Hi_score.txt','w') as file:
                        file.write(str(Hi_score))

# Program to reset Hi_score:

reset=input('Enter yes to reset high score :')  # Asking user if he/she wants to reset high score
if (reset=='yes'):
    with open('Hi_score.txt','w') as file:
        file.write('0')

