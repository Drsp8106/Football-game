'''
Derek Phillips
DTS-190 project
Football Game
'''
import projectfunctions as f
import random
print('Welcome to My Football game!')
print('Here you start with the ball.')

cputype = ['run','pass'] #cpu play type
compchoice = random.choice(cputype)

playerdrive = 1
computerdrive = 1
while playerdrive != 8:
    f.down = 1
    f.yardline = 25
    f.cpudown = 1
    f.cpuyardline = 25
    cputd = 'no'
    td = 'no'
    while td != 'yes' and f.down <= 4:
        if f.yardline >= 100: #checks if they scored a td
            f.playerscore = f.playerscore + 7 #I had to look this up to update the count, but it works similar to using other import functions
            playerdrive = playerdrive + 1 
            td = 'yes'
            print (f'Your scored a touchdown! The score is now {f.playerscore}(you) to {f.computerscore}(computer)\nIt is now the computers turn')
        else:
            type = input('would you like to run or pass? ')
            print(f.playcall(type))
    while cputd != 'yes' and f.cpudown <=4:
        if f.cpuyardline >= 100: #checks if they scored a td
            f.computerscore = f.computerscore + 7 #I had to look this up to update the count, but it works similar to using other import functions
            playerdrive = playerdrive + 1 
            cputd = 'yes'
            print(f'computer scored a touchdown, The score is now {f.playerscore}(you) to {f.computerscore}(computer)\nyour turn!')
        else:
            print(f.cputurn(compchoice))
print(f'The final score is {f.playerscore}(you) to {f.computerscore}(computer)')
if f.playerscore > f.computerscore:
    print('Congratulations, you Win!!!')
elif f.computerscore > f.playerscore:
    print('Ohhhh you lost to the computer, Better luck next time!')
