import argparse
import sys

sys.path.append("src")
from GameController import GameController


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Chinese Checkers game with AI and player options.')
    # Required player count selection
    parser.add_argument('--players', type=int, choices=[2, 4], required=True,
                       help='Number of players (2 or 4)')

    parser.add_argument('--first-player', choices=['human', 'minimax'], required=False,
                        help='Type of the first player (bottom-left).')
    parser.add_argument('--first-minimax-depth', type=int, default=3, required=False,
                        help='Minimax depth for the first player, if applicable.')
    #parser.add_argument('--second-player', choices=['random', 'nonrepeatrandom', 'minimax'], required=False,
    #                    help='Type of the second player.')
    parser.add_argument('--second-player', choices=['human','minimax'], required=False,
                        help='Type of the second player.')
    parser.add_argument('--second-minimax-depth', type=int, default=3, required=False,
                        help='Minimax depth for the second player, if applicable.')
    
    parser.add_argument('--third-player', choices=['human', 'minimax'], default='minimax',
                       help='Type of the third player (top-left) - required for 4 players')
    parser.add_argument('--third-minimax-depth', type=int, default=3,
                       help='Minimax depth for player 3 if AI')
    
    parser.add_argument('--fourth-player', choices=['human', 'minimax'], default='minimax',
                       help='Type of player 4 (bottom-right)')
    parser.add_argument('--fourth-minimax-depth', type=int, default=3,
                       help='Minimax depth for player 4 if AI')
    
    '''
    parser.add_argument('--player1', choices=['human', 'minimax'], default='human',
                       help='Type of player 1 (bottom-left)')
    parser.add_argument('--player1-depth', type=int, default=3,
                  5     help='Minimax depth for player 1 if AI')
    
    parser.add_argument('--player2', choices=['human', 'minimax'], default='minimax',
                       help='Type of player 2 (top-right)')
    parser.add_argument('--player2-depth', type=int, default=3,
                       help='Minimax depth for player 2 if AI')

    ''' 
    args = parser.parse_args()

     # Validate player count matches provided players
    if args.players == 4 and (args.third_player is None or args.fourth_player is None):
        parser.error("--third-player and --fourth-player required for 4-player mode")
    elif args.players == 2 and (args.third_player is not None or args.fourth_player is not None):
        print("Warning: Ignoring third/fourth player arguments for 2-player mode")


    controller = GameController(verbose=False, use_graphics=True, args=args)

    controller.game_loop()
