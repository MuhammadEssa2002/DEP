import game_class as gc
import argparse

def main():
    parser = argparse.ArgumentParser(description='Red-Blue Nim Game Coded by M.Essa')
    parser.add_argument('-r','--num-red', type=int, default=10,metavar=' ',help='Number of red marbles (default: 10)')
    parser.add_argument('-b','--num-blue', type=int, default=8, metavar='',help='Number of blue marbles (default: 8)')
    parser.add_argument('-v','--version', choices=['standard','misere'], default='standard',metavar='', help='Game version to play standard or misere (default: standard)')
    parser.add_argument('-f','--first', choices=['player','computer'], default='computer',metavar='', help='Who goes first computer or player (default: computer)')
    parser.add_argument('-d','--depth', type=int, default=10, metavar='',help='Depth of minimax search (default: 10)')
    args = parser.parse_args()


    if args.version == 'standard':
        version_choies = True
    else:
        version_choies = False

    first_p = args.first
    if first_p == 'player':
        first_p = True
    else:
        first_p = False

    computer = gc.Version(None,args.depth,version_choies)
    player = gc.First_player(not first_p,first_p)
    state = [args.num_red,args.num_blue]
    game = gc.Game(state,computer,player)
    game.start_game()
if __name__ == '__main__':
    main()  
