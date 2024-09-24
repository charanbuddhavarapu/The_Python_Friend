import random

comp= ['rock','paper','scissor']


user=0
computer = 0

while True:
    comp_choice = random.choice(comp)
    print("computer's choise is : ",comp_choice)
    user_input=input('Please Enter your selection in rock/paper/scissor ').lower()
    
    if user_input not in comp:
        print('Please select a valid choice')
        continue
    else:
        if user_input == 'rock' and comp_choice =='scissor':
             user+=1
             print(user,computer)
        elif user_input == 'scissor' and comp_choice =='paper':
            user+=1
            print(user,computer)
        elif user_input == 'paper' and comp_choice =='scissor':
            user+=1
            print(user,computer)

       
        else:
            computer+=1
            print(user,computer)

        
        
    if user ==5 or computer==5:
        print("GAME OVER",)
        quit()
    else: continue