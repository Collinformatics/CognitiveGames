import argparse
from functions import *
from mathematics import Math
from memory import Memory


parser = argparse.ArgumentParser(description='Cognitive Games')
parser.add_argument('--math', action='store_true',
                    help='Begin with the mathematics games')
parser.add_argument('-m', '--maxvalue', type=int, default=15,
                    help='Max value for the operation tables (default=15)')
parser.add_argument('-r', '--randomize', action='store_false',
                    help='Decrease difficulty by ordering tables')
parser.add_argument('--memory', action='store_true',
                    help='Begin with the memory games')
parser.add_argument('-t', '--timer', type=float, default=1.0,
                    help='Amount of time in seconds a digit is displayed '
                         'in a memory game (default=1 sec)')
args = parser.parse_args()


# Initialize classes
mathGames = Math(maxValue=args.maxvalue, randomize=args.randomize)
memoryGames = Memory(timer=args.timer)

# Options
games = {
    '1': 'Mathematics',
    '2': 'Memory',
    'q': 'Quit'
}

# Startup options
if args.math:
    mathGames.run()
if args.memory:
    memoryGames.run()


if __name__ == '__main__':
    while True:
        exercise = question(games)
        if exercise == 'Mathematics':
            mathGames.run()
        elif exercise == 'Memory':
            memoryGames.run()
        else:
            break
