import random
import Project as p
run_in_options = [1,2,3,4,5,6,7,8] #list to randomly pick outcome of a play for the runs and passes
run_out_options = [3,4,5,6,7,8,9,10,11,12]
pass_short_options = [6,7,8,9,10]
pass_medium_options = [12,13,14,15,16,0,0]#0s mean incomplete
pass_long_options = [25,30,32,33,50,52,60,0,0,0,]
yardline = 25 #what yardline they are on 
down = 1 #what down they are on 
yards2first = 10 #using this to subtract the play from it, to determine how many yards to a first down
playerscore = 0 #player and computer score
computerscore = 0

cpuyardline = 25 #what yardline they are on 
cpudown = 1 #what down they are on 
cpuyards2first = 10 
cpurun = ['inside','outside']
cpupass = ['short','medium','long']
cpurun_in_options = [1,2,3,0,0] #list to randomly pick outcome of a play for the runs and passes
cpurun_out_options = [3,4,5,6,0,0,]
cpupass_short_options = [6,7,0,0,0]
cpupass_medium_options = [0,13,14,15,0,0,0]#0s mean incomplete
cpupass_long_options = [25,30,32,33,0,0,0,0]#more 0s through all these to make the game easier

def playcall(x):
    global yardline #using global to change within variable in the function
    global yards2first
    global down
    global playerscore
    down = down + 1
    if down>4:#checks what down it is
        return ("you turn it over on downs, computers turn!")
    if x == 'run':#loop for player decision
        in_out= input('would you like to run inside or outside? ')
        if in_out == 'inside':
            play = random.choice(run_in_options)
            yardline = yardline + int(play)
            yards2first = yards2first - int(play)
            if yards2first <= 0:
                yards2first = 10
                down = 1
                return (f'You run for {play} yards, to the {yardline} \nThats enough for a first down')
            else:
                return (f"You run for {play} yards, to the {yardline} \nIt's {down} down")
            
        elif in_out == 'outside':
            play = random.choice(run_out_options)
            yardline = yardline + int(play)
            yards2first = yards2first - int(play)
            if yards2first <= 0:
                yards2first = 10
                down = 1
                return (f'You run for {play} yards, to the {yardline} \n Thats enough for a first down')
            else:
                return (f"You run for {play} yards, to the {yardline} \n It's {down} down")
    elif x == 'pass':
        passdepth = input('Would you like to pass short, medium, or long ')
        if passdepth == 'short':
            play = random.choice(pass_short_options)
            yardline = yardline + int(play)
            yards2first = yards2first - int(play)
            if yards2first <= 0:
                yards2first = 10
                down = 1
                return (f'You pass for {play} yards, to the {yardline} \nThats enough for a first down')
            else:
                return (f"You pass for {play} yards, to the {yardline} \nIt's {down} down")
        if passdepth == 'medium':
            play = random.choice(pass_medium_options)
            yardline = yardline + int(play)
            yards2first = yards2first - int(play)
            if yards2first <= 0:
                yards2first = 10
                down = 1
                return (f'You pass for {play} yards, to the {yardline} \nThats enough for a first down')
            else:
                return (f"You pass for {play} yards, to the {yardline} \nIt's {down} down")
        if passdepth == 'long':
            play = random.choice(pass_long_options)
            yardline = yardline + int(play)
            yards2first = yards2first - int(play)
            if yards2first <= 0:
                yards2first = 10
                down = 1
                return (f'You pass for {play} yards, to the {yardline} \nThats enough for a first down')
            else:
                return (f"You pass for {play} yards, to the {yardline} \nIt's {down} down")
    else:
        return "you did not put in a valid play option"
    

def cputurn(x):
    global cpuyardline #using global to change within variable in the function
    global cpuyards2first
    global cpudown
    global computerscore
    cpudown = cpudown + 1
    if cpudown>4:#checks what down it is
        return ("Computer turns it over on downs, Your turn!")
    if x == 'run':#loop for computer decision
        in_out= random.choice(cpurun)
        if in_out == 'inside':
            play = random.choice(cpurun_in_options)
            cpuyardline = cpuyardline + int(play)
            cpuyards2first = cpuyards2first - int(play)
            if cpuyards2first <= 0:
                cpuyards2first = 10
                cpudown = 1
                return (f'Computer runs for {play} yards, to the {cpuyardline} \nThats enough for a first down')
            else:
                return (f"Computer runs for {play} yards, to the {cpuyardline} \nIt's {cpudown} down")
            
        elif in_out == 'outside':
            play = random.choice(cpurun_out_options)
            cpuyardline = cpuyardline + int(play)
            cpuyards2first = cpuyards2first - int(play)
            if cpuyards2first <= 0:
                cpuyards2first = 10
                down = 1
                return (f'Computer runs for {play} yards, to the {cpuyardline} \n Thats enough for a first down')
            else:
                return (f"Computer runs for {play} yards, to the {cpuyardline} \n It's {cpudown} down")
    elif x == 'pass':
        passdepth = random.choice(cpupass)
        if passdepth == 'short':
            play = random.choice(cpupass_short_options)
            cpuyardline = cpuyardline + int(play)
            cpuyards2first = cpuyards2first - int(play)
            if cpuyards2first <= 0:
                cpuyards2first = 10
                cpudown = 1
                return (f'Computer passses for {play} yards, to the {cpuyardline} \nThats enough for a first down')
            else:
                return (f"Computer passes for {play} yards, to the {cpuyardline} \nIt's {cpudown} down")
        if passdepth == 'medium':
            play = random.choice(cpupass_medium_options)
            cpuyardline = cpuyardline + int(play)
            cpuyards2first = cpuyards2first - int(play)
            if cpuyards2first <= 0:
                cpuyards2first = 10
                cpudown = 1
                return (f'You pass for {play} yards, to the {cpuyardline} \nThats enough for a first down')
            else:
                return (f"You pass for {play} yards, to the {cpuyardline} \nIt's {cpudown} down")
        if passdepth == 'long':
            play = random.choice(cpupass_long_options)
            cpuyardline = cpuyardline + int(play)
            cpuyards2first = cpuyards2first - int(play)
            if cpuyards2first <= 0:
                cpuyards2first = 10
                cpudown = 1
                return (f'Computer passes for {play} yards, to the {cpuyardline} \nThats enough for a first down')
            else:
                return (f"Computer passes for {play} yards, to the {cpuyardline} \nIt's {cpudown} down")
