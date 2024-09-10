import game_class as gc



# Game 1 is a standard game where the Human play first who takes the last marble wins
############################################################################################
def game_1(state,comp,player,state_red,state_blue):
    
    mesg = gc.message(state[0],state[1],player)
    
    # if player.human_error:
    #     print(player.error_gc.message())
    #     player.get_human_error()
    #     game_1(state,comp,player,state_red,state_blue)
    # else: 
    if player.first_human():
            mesg.get_message_state_1()
            player.change_first()
    else:
            mesg.get_message_state_2(state_red,state_blue)
        
        
    
    
   
    red_blue = input(f'Which Marbles you want to take out Red or Blue:- ')
    
    if red_blue.lower() == 'red':
        take = input(f'Input the value of Red Marbles, you want to take out:- ')
        if take.isdigit() == False: 
            player.get_human_error()
            player.error('Please input a number')
            return game_1(state,comp,player,state_red,state_blue)
        take = int(take)
        if abs(take) > state[0]:
            player.get_human_error()
            player.error(f'Sorry in Red only {state[0]} Marbles are left')
            return game_1(state,comp,player,state_red,state_blue)
        if take > 2 or take < 1:
            player.get_human_error()
            player.error('Sorry you can only take out 1 or 2 balls')
            return game_1(state,comp,player,state_red,state_blue)
        state[0] = state[0] - take
    elif red_blue.lower() == 'blue':
        take = input(f'Input the value of Blue Marbles, you want to take out:- ')
        if take.isdigit() == False: 
            player.get_human_error()
            player.error('Please input a number')
            return game_1(state,comp,player,state_red,state_blue)
        take = int(take)
        if abs(take) > state[1]:
            player.get_human_error()
            player.error(f'Sorry in Blue only {state[1]} Marbles are left')
            return game_1(state,comp,player,state_red,state_blue)
        if take > 2 or take < 1:
            player.get_human_error()
            player.error('Sorry you can only take out 1 or 2 balls')
            return game_1(state,comp,player,state_red,state_blue)
        state[1] = state[1] - take
    else:
        player.get_human_error()
        player.error('Sorry you can only choose Red or Blue')
        return game_1(state,comp,player,state_red,state_blue)
    
    
    if player.human_error:
        player.get_human_error()
    
    if state[0]*state[1] == 0:
        if state[0] != 0:
            mesg.human_won_message("Red",state[0])
            return None
        else:
            mesg.human_won_message("Blue",state[1])
            return None
        
        
    new_state = (state[0],state[1])
    comp.update_states(new_state)
    selected_move = comp.get_next_move()
    selected_move = selected_move[1]
    state_red = state[0] - selected_move[0]
    state_blue = state[1] - selected_move[1]
    state[0] = state[0] - state_red
    state[1] = state[1] - state_blue
    if state[0]*state[1] == 0:
        if state[0] != 0:
            mesg.computer_won_message("Red",state[0])
            
            return None
        else:
            mesg.computer_won_message("Blue",state[1])
            return None
    
    return game_1(state,comp,player,state_red,state_blue)
############################################################################################         


# Game 2 is a standard game where the Computer play first who takes the last marble wins
############################################################################################
def game_2(state,comp,player,state_red,state_blue):
    
    
    
    
    if player.first_computer():
        new_state = (state[0],state[1])
        comp.update_states(new_state)
        selected_move = comp.get_next_move()
        selected_move = selected_move[1]
        state_red = state[0] - selected_move[0]
        state_blue = state[1] - selected_move[1]
        state[0] = state[0] - state_red
        state[1] = state[1] - state_blue
        player.change_first()
    
    mesg = gc.message(state[0],state[1],player)
    
    if state[0]*state[1] == 0:
        if state[0] != 0:
            mesg.computer_won_message("Red",state[0])
            return None
        else:
            mesg.computer_won_message("Blue",state[1])
            return None     
    
    
    if player.first_computer():
            mesg.get_message_state_1()
    else:
            mesg.get_message_state_2(state_red,state_blue)
        
        
    
    
   
    red_blue = input(f'Which Marbles you want to take out Red or Blue:- ')
    
    if red_blue.lower() == 'red':
        take = input(f'Input the value of Red Marbles, you want to take out:- ')
        if take.isdigit() == False: 
            player.get_human_error()
            player.error('Please input a number')
            return game_2(state,comp,player,state_red,state_blue)
        take = int(take)
        if abs(take) > state[0]:
            player.get_human_error()
            player.error(f'Sorry in Red only {state[0]} Marbles are left')
            return game_2(state,comp,player,state_red,state_blue)
        if take > 2 or take < 1:
            player.get_human_error()
            player.error('Sorry you can only take out 1 or 2 balls')
            return game_2(state,comp,player,state_red,state_blue)
        state[0] = state[0] - take
    elif red_blue.lower() == 'blue':
        take = input(f'Input the value of Blue Marbles, you want to take out:- ')
        if take.isdigit() == False: 
            player.get_human_error()
            player.error('Please input a number')
            return game_2(state,comp,player,state_red,state_blue)
        take = int(take)
        if abs(take) > state[1]:
            player.get_human_error()
            player.error(f'Sorry in Blue only {state[1]} Marbles are left')
            return game_2(state,comp,player,state_red,state_blue)
        if take > 2 or take < 1:
            player.get_human_error()
            player.error('Sorry you can only take out 1 or 2 balls')
            return game_2(state,comp,player,state_red,state_blue)
        state[1] = state[1] - take
    else:
        player.get_human_error()
        player.error('Sorry you can only choose Red or Blue')
        return game_2(state,comp,player,state_red,state_blue)


    
    
    if state[0]*state[1] == 0:
        if state[0] != 0:
            mesg.human_won_message("Red",state[0])
            return None
        else:
            mesg.human_won_message("Blue",state[1])
            return None  
    
    if player.human_error:
        player.get_human_error()
    player.change_first()
    
    
    return game_2(state,comp,player,state_red,state_blue)
############################################################################################


# Game 3 is a misere game where the Human play first who takes the last marble loses
############################################################################################
def game_3(state,comp,player,state_red,state_blue):
    
    mesg = gc.message(state[0],state[1],player)
    
    # if player.human_error:
    #     print(player.error_gc.message())
    #     player.get_human_error()
    #     game_3(state,comp,player,state_red,state_blue)
    # else: 
    if player.first_human():
            mesg.get_message_state_3()
            player.change_first()
    else:
            mesg.get_message_state_4(state_red,state_blue)
        
        
    
      
    red_blue = input(f'Which Marbles you want to take out Red or Blue:- ')
    
    if red_blue.lower() == 'red':
        take = input(f'Input the value of Red Marbles, you want to take out:- ')
        if take.isdigit() == False: 
            player.get_human_error()
            player.error('Please input a number')
            return game_3(state,comp,player,state_red,state_blue)
        take = int(take)
        if abs(take) > state[0]:
            player.get_human_error()
            player.error(f'Sorry in Red only {state[0]} Marbles are left')
            return game_3(state,comp,player,state_red,state_blue)
        if take > 2 or take < 1:
            player.get_human_error()
            player.error('Sorry you can only take out 1 or 2 balls')
            return game_3(state,comp,player,state_red,state_blue)
        state[0] = state[0] - take
    elif red_blue.lower() == 'blue':
        take = input(f'Input the value of Blue Marbles, you want to take out:- ')
        if take.isdigit() == False: 
            player.get_human_error()
            player.error('Please input a number')
            return game_3(state,comp,player,state_red,state_blue)
        take = int(take)
        if abs(take) > state[1]:
            player.get_human_error()
            player.error(f'Sorry in Blue only {state[1]} Marbles are left')
            return game_3(state,comp,player,state_red,state_blue)
        if take > 2 or take < 1:
            player.get_human_error()
            player.error('Sorry you can only take out 1 or 2 balls')
            return game_3(state,comp,player,state_red,state_blue)
        state[1] = state[1] - take
    else:
        player.get_human_error()
        player.error('Sorry you can only choose Red or Blue')
        return game_3(state,comp,player,state_red,state_blue)

    
    if player.human_error:
        player.get_human_error()
    
    if state[0]*state[1] == 0:
        if state[0] != 0:
            mesg.computer_won_message("Red",state[0])
            return None
        else:
            mesg.computer_won_message("Blue",state[1])
            return None
        
    new_state = (state[0],state[1])
    comp.update_states(new_state)
    selected_move = comp.get_next_move()
    selected_move = selected_move[1]
    state_red = state[0] - selected_move[0]
    state_blue = state[1] - selected_move[1]
    state[0] = state[0] - state_red
    state[1] = state[1] - state_blue
    if state[0]*state[1] == 0:
        if state[0] != 0:
            mesg.human_won_message("Red",state[0])
            return None
        else:
            mesg.human_won_message("Blue",state[1])
            return None
    
    return game_3(state,comp,player,state_red,state_blue)
############################################################################################


# Game 4 is a misere game where the Computer play first who takes the last marble loses
############################################################################################
def game_4(state,comp,player,state_red,state_blue):

    if player.first_computer():
        new_state = (state[0],state[1])
        comp.update_states(new_state)
        selected_move = comp.get_next_move()
        selected_move = selected_move[1]
        state_red = state[0] - selected_move[0]
        state_blue = state[1] - selected_move[1]
        state[0] = state[0] - state_red
        state[1] = state[1] - state_blue
        player.change_first()
    
    mesg = gc.message(state[0],state[1],player)
    
    if state[0]*state[1] == 0:
        if state[0] != 0:
            mesg.human_won_message("Red",state[0])
            return None
        else:
            mesg.human_won_message("Blue",state[1])
            return None  

    
    
    
    if player.first_computer():
            mesg.get_message_state_3()
    else:
            mesg.get_message_state_4(state_red,state_blue)
        
        
    

    red_blue = input(f'Which Marbles you want to take out Red or Blue:- ')
    
    if red_blue.lower() == 'red':
        take = input(f'Input the value of Red Marbles, you want to take out:- ')
        if take.isdigit() == False: 
            player.get_human_error()
            player.error('Please input a number')
            return game_4(state,comp,player,state_red,state_blue)
        take = int(take)
        if abs(take) > state[0]:
            player.get_human_error()
            player.error(f'Sorry in Red only {state[0]} Marbles are left')
            return game_4(state,comp,player,state_red,state_blue)
        if take > 2 or take < 1:
            player.get_human_error()
            player.error('Sorry you can only take out 1 or 2 balls')
            return game_4(state,comp,player,state_red,state_blue)
        state[0] = state[0] - take
    elif red_blue.lower() == 'blue':
        take = input(f'Input the value of Blue Marbles, you want to take out:- ')
        if take.isdigit() == False: 
            player.get_human_error()
            player.error('Please input a number')
            return game_4(state,comp,player,state_red,state_blue)
        take = int(take)
        if abs(take) > state[1]:
            player.get_human_error()
            player.error(f'Sorry in Blue only {state[1]} Marbles are left')
            return game_4(state,comp,player,state_red,state_blue)
        if take > 2 or take < 1:
            player.get_human_error()
            player.error('Sorry you can only take out 1 or 2 balls')
            return game_4(state,comp,player,state_red,state_blue)
        state[1] = state[1] - take
    else:
        player.get_human_error()
        player.error('Sorry you can only choose Red or Blue')
        return game_4(state,comp,player,state_red,state_blue)

    if state[0]*state[1] == 0:
        if state[0] != 0:
            mesg.computer_won_message("Red",state[0])
            return None
        else:
            mesg.computer_won_message("Blue",state[1])
            return None     
        
        
    if player.human_error:
        player.get_human_error()
    player.change_first()
    
    
    return game_4(state,comp,player,state_red,state_blue)
############################################################################################


def main():
    pass
if __name__ == '__main__':
    main()  