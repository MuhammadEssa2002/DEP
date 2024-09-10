import minimax as mnimx
import game_version as gv
import os
clear = lambda: os.system('cls')


class Num_red:
    def __init__(self, num):
        self.num = num
        
    def get_num(self):
        return self.num

  
class Num_blue:
    def __init__(self, num):
        self.num = num

    def get_num(self):
        return self.num
    
    
class Version:
    def __init__(self, state=None,depth = 20,standard=True):
        self.state = state
        self.depth = depth
        self.standard = standard
    
    def update_states(self,new_state):
        self.state = new_state
    
    def get_next_move(self):
        if self.standard:
            return mnimx.next_move_standard(self.state,self.depth)
        else:
            return mnimx.next_move_misere(self.state,self.depth)
        
class First_player:
    def __init__(self, computer = False, human = True,human_error = False):
        self.computer = computer
        self.human = human
        self.human_error = human_error
        self.human_error_message = None
    def first_computer(self):
        return self.computer
    
    def first_human(self):
        return self.human
    
    def change_first(self):
        self.computer = not self.computer
        self.human = not self.human
        return None
    
    def get_human_error(self):
        self.human_error = not self.human_error
        return None
        
    def error(self,Error):
        self.human_error_message = Error
        return None
    
    def error_message(self):
        return self.human_error_message
        
    
        

class message:
    def __init__(self,red,blue,player):
        self.red = red
        self.blue = blue
        self.player = player
    def get_message_state_1(self):
        clear()
        print(f'<<<<<<Game Version is Standard>>>>>>')
        print(f'<<If You take the last  Red or Blue Marble then You Win>>\n')
        print(f'{self.red} Red Marbles and {self.blue} Blue Marbles remaining \n')
        print("Red Marbles " + self.red*"*")
        print("Blue Marbles " + self.blue*"*")
        print(f'\nYour Turn')
        return None
    def get_message_state_2(self,state_red,state_blue):
        clear()
        if self.player.human_error:
            print(f'<<<<<<Game Version is Standard>>>>>>')
            print(f'<<If You take the last  Red or Blue Marble then You Win>>\n')
            print(f'{self.red} Red Marbles and {self.blue} Blue Marbles remaining \n')
            print("Red Marbles " + self.red*"*")
            print("Blue Marbles " + self.blue*"*")
            print(f'Type Error ---> ({self.player.error_message()})\n')
            print(f'\nYour Turn')
            self.player.get_human_error()
        else:
            print(f'<<<<<<Game Version is Standard>>>>>>')
            print(f'<<If You take the last  Red or Blue Marble then You Win>>\n')
            print(f'Computer took out {state_red} Red Marbles and {state_blue} Blue Marbles')
            print(f'{self.red} Red Marbles and {self.blue} Blue Marbles remaining \n')
            print("Red Marbles " + self.red*"*")
            print("Blue Marbles " + self.blue*"*")
            print(f'\nYour Turn')
        return None
    def get_message_state_3(self):
        clear()
        print(f'<<<<<<Game Version is Misere>>>>>>')
        print(f'<<If You take the last  Red or Blue Marble then You Lose>>\n')
        print(f'{self.red} Red Marbles and {self.blue} Blue Marbles remaining \n')
        print("Red Marbles " + self.red*"*")
        print("Blue Marbles " + self.blue*"*")
        print(f'\nYour Turn')
        return None
    
    def get_message_state_4(self,state_red,state_blue):
        clear()
        if self.player.human_error:
            print(f'<<<<<<Game Version is Misere>>>>>>')
            print(f'<<If You take the last  Red or Blue Marble then You Lose>>\n')
            print(f'{self.red} Red Marbles and {self.blue} Blue Marbles remaining \n')
            print("Red Marbles " + self.red*"*")
            print("Blue Marbles " + self.blue*"*")
            print(f'Type Error ---> ({self.player.error_message()})\n')
            print(f'\nYour Turn')
            self.player.get_human_error()
        else:
            print(f'<<<<<<Game Version is Misere>>>>>>')
            print(f'<<If You take the last  Red or Blue Marble then You Lose>>\n')
            print(f'Computer took out {state_red} Red Marbles and {state_blue} Blue Marbles')
            print(f'{self.red} Red Marbles and {self.blue} Blue Marbles remaining \n')
            print("Red Marbles " + self.red*"*")
            print("Blue Marbles " + self.blue*"*")
            print(f'\nYour Turn')
        return None
    def human_won_message(self,color,score):
        clear()
        if color.lower() == 'red':
            print("""
                  ██╗  ██╗██╗   ██╗██████╗ ██████╗  █████╗ ██╗   ██╗██╗    ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗ ██████╗ ███╗   ██╗
                  ██║  ██║██║   ██║██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝██║    ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██╔═══██╗████╗  ██║
                  ███████║██║   ██║██████╔╝██████╔╝███████║ ╚████╔╝ ██║     ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║   ██║██╔██╗ ██║
                  ██╔══██║██║   ██║██╔══██╗██╔══██╗██╔══██║  ╚██╔╝  ╚═╝      ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║   ██║██║╚██╗██║
                  ██║  ██║╚██████╔╝██║  ██║██║  ██║██║  ██║   ██║   ██╗       ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝╚██████╔╝██║ ╚████║
                  ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝       ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═══╝
                                                                                                                     """)
            print(f'<<<<<<Final Score is {2*score}>>>>>>')
        elif color.lower() == 'blue':
            print("""
                  ██╗  ██╗██╗   ██╗██████╗ ██████╗  █████╗ ██╗   ██╗██╗    ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗ ██████╗ ███╗   ██╗
                  ██║  ██║██║   ██║██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝██║    ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██╔═══██╗████╗  ██║
                  ███████║██║   ██║██████╔╝██████╔╝███████║ ╚████╔╝ ██║     ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║   ██║██╔██╗ ██║
                  ██╔══██║██║   ██║██╔══██╗██╔══██╗██╔══██║  ╚██╔╝  ╚═╝      ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║   ██║██║╚██╗██║
                  ██║  ██║╚██████╔╝██║  ██║██║  ██║██║  ██║   ██║   ██╗       ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝╚██████╔╝██║ ╚████║
                  ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝       ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═══╝
                                                                                                                     """)
            print(f'<<<<<<Final Score is {3*score}>>>>>>')
        return None
    def computer_won_message(self,color,score):
        clear()
        if color.lower() == 'red':
            print(""" 
                       ██████╗ ██████╗ ███╗   ███╗██████╗ ██╗   ██╗████████╗███████╗██████╗         ██╗    ██╗ ██████╗ ███╗   ██╗
                      ██╔════╝██╔═══██╗████╗ ████║██╔══██╗██║   ██║╚══██╔══╝██╔════╝██╔══██╗        ██║    ██║██╔═══██╗████╗  ██║
                      ██║     ██║   ██║██╔████╔██║██████╔╝██║   ██║   ██║   █████╗  ██████╔╝        ██║ █╗ ██║██║   ██║██╔██╗ ██║
                      ██║     ██║   ██║██║╚██╔╝██║██╔═══╝ ██║   ██║   ██║   ██╔══╝  ██╔══██╗        ██║███╗██║██║   ██║██║╚██╗██║
                      ╚██████╗╚██████╔╝██║ ╚═╝ ██║██║     ╚██████╔╝   ██║   ███████╗██║  ██║        ╚███╔███╔╝╚██████╔╝██║ ╚████║
                       ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝      ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝         ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═══╝  """)
            print(f'<<<<<<Final Score is {2*score}>>>>>>')
        elif color.lower() == 'blue':
            print("""
                       ██████╗ ██████╗ ███╗   ███╗██████╗ ██╗   ██╗████████╗███████╗██████╗         ██╗    ██╗ ██████╗ ███╗   ██╗
                      ██╔════╝██╔═══██╗████╗ ████║██╔══██╗██║   ██║╚══██╔══╝██╔════╝██╔══██╗        ██║    ██║██╔═══██╗████╗  ██║
                      ██║     ██║   ██║██╔████╔██║██████╔╝██║   ██║   ██║   █████╗  ██████╔╝        ██║ █╗ ██║██║   ██║██╔██╗ ██║
                      ██║     ██║   ██║██║╚██╔╝██║██╔═══╝ ██║   ██║   ██║   ██╔══╝  ██╔══██╗        ██║███╗██║██║   ██║██║╚██╗██║
                      ╚██████╗╚██████╔╝██║ ╚═╝ ██║██║     ╚██████╔╝   ██║   ███████╗██║  ██║        ╚███╔███╔╝╚██████╔╝██║ ╚████║
                       ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝      ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝         ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═══╝  """)
            print(f'<<<<<<Final Score is {3*score}>>>>>>')
        return None
    
        
        

class Game:
    def __init__(self,state,computer,player):
        self.state = state
        self.computer = computer
        self.player = player
        self.state_red = 0
        self.state_blue = 0
    def start_game(self):
        if self.computer.standard:
            if self.player.human:
                gv.game_1(self.state,self.computer,self.player,self.state_red,self.state_blue)
            else:
                gv.game_2(self.state,self.computer,self.player,self.state_red,self.state_blue)
        else:
            if self.player.human:
                gv.game_3(self.state,self.computer,self.player,self.state_red,self.state_blue)
            else:
                gv.game_4(self.state,self.computer,self.player,self.state_red,self.state_blue)
    
        


def main():
    red_marbles = Num_red(5)
    blue_marbles = Num_blue(6)
    comm = True
    state = [red_marbles.get_num(),blue_marbles.get_num()]
    first_player = First_player(comm,not comm)
    computer = Version(None, False)
    gv.game_4(state,computer,first_player,0,0)
if __name__ == '__main__':
    main()       