from functions import *
import random
import readline
import sys
import termios
import time


"""
    Improve your working memory with digit span games
"""


# Colors
red = '\033[31m'
cyan = '\033[36m'
pink = '\033[35m'
rst = '\033[0m'


class Memory:
    def __init__(self, timer):
        self.maxLen = 10
        self.minLen = 4
        self.timer = timer
        self.games = {
            '0': 'Set Parameters',
            '1': 'Digit Span',
            '2': 'Digit Span Reversed',
            '3': 'Ordered Digit Span',
            'h': 'Help',
            'e': 'End Game',
            'q': 'Quit'
        }
        self.instructions = {
            'Digit Span': 'Memorize a number sequence in their sequential order',
            'Digit Span Reversed': 'Memorize a number sequence and then reverse their '
                                   'sequential order',
            'Ordered Digit Span': 'Memorize a number sequence and then arrange the '
                                  'values in an increasing order from 0 to 9',
        }


    @staticmethod
    def quiz(digit):
        # Get answer
        correct = False
        while True:
            answer = input('What was the value: ')
            if answer:
                if answer == digit:
                    correct = True
                deleteLine()
                break
            deleteLine()

        # Verify
        if not correct:
            x = ''
            for i in range(len(digit)):
                try:
                    if digit[i] != answer[i]:
                        x += f'{red}{answer[i]}{rst}'
                    else:
                        x += answer[i]
                except:
                    x += f'{red}-{rst}'
            print(f'Incorrect answer\n'
                  f'* Number: {digit}\n'
                  f'* Answer: {x}')
        return correct


    def run(self):
        while True:
            printBar()
            exercise = question(params=self.games)
            if exercise == 'Set Parameters':
                self.params()
            if exercise == 'Digit Span':
                self.digitSpan(exercise)
            elif exercise == 'Digit Span Reversed':
                self.digitSpanRev(exercise)
            elif exercise == 'Ordered Digit Span':
                self.digitSpanOrdered(exercise)
            elif exercise == 'Help':
                helpMe(self.instructions, 'Digit Memorization')
            elif exercise == 'End Game':
                printBar()
                break
            else:
                sys.exit()


    def params(self):
        delLine = 7
        distance = 5
        while True:
            limUpper = self.maxLen - distance
            limLower = self.minLen + distance
            params = {
                '0': 'Done',
                '1': f'Maximum Length: {cyan}{self.maxLen}{rst}',
                '2': f'Minimum Length: {cyan}{self.minLen}{rst}',
                '3': f'Time Limit: {cyan}{self.timer} sec{rst}'
            }

            print('Change Parameter:')
            for k, v in params.items():
                print(f'  {k}: {v}')
            x = input('Select Option: ')
            if x in params.keys():
                if x == '0':
                    break
                elif x == '1':
                    v = getInput(f'Maximum Digit Length (min={limLower}): ', int)
                    if isinstance(v, int):
                        if v >= limLower:
                            self.maxLen = v
                elif x == '2':
                    v = getInput(f'Minimum Digit Length (max={limUpper}): ', int)
                    if isinstance(v, int):
                        if v <= limUpper:
                            self.minLen = v
                elif x == '3':
                    v = getInput(f'Set Time Limit (min=1): ', float)
                    if isinstance(v, float):
                        if v > 0:
                            self.timer = v
                deleteLine(nLines=delLine)
            else:
                deleteLine(nLines=delLine-1)


    def getSequences(self):
        def genDigit(lim):
            d = str(random.randint(0, 9))
            for _ in range(lim-1):
                d += str(random.randint(0, 9))
            return d

        values = []
        l = self.minLen
        while True:
            values.append(genDigit(l))
            values.append(genDigit(l))
            l += 1
            if l > self.maxLen:
                break

        countdown()

        return values


    def displayValue(self, digit):
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)

        # Block terminal input
        tmpSetting = termios.tcgetattr(fd)
        tmpSetting[3] &= ~termios.ECHO
        termios.tcsetattr(fd, termios.TCSANOW, tmpSetting)

        try:
            for d in digit:
                print(f'\n  {cyan}{d}{rst}')
                time.sleep(self.timer)
                deleteLine(nLines=2)
                print('\n')
                time.sleep(0.25)
                deleteLine(nLines=2)
        finally:
            # Restore terminal
            termios.tcsetattr(fd, termios.TCSANOW, old_settings)
            # Flush any input that was typed during the animation
            termios.tcflush(fd, termios.TCIOFLUSH)


    def digitSpan(self, drill):
        printBar(drill)
        numbers = self.getSequences()
        for i, value in enumerate(numbers):
            self.displayValue(value)
            correct = self.quiz(digit=value)
            if not correct:
                print(f'You correctly recalled {i} / {len(numbers)} values')
                return


    def digitSpanRev(self, drill):
        printBar(drill)
        numbers = self.getSequences()
        for i, value in enumerate(numbers):
            self.displayValue(value)
            correct = self.quiz(digit=value[::-1])
            if not correct:
                print(f'You correctly recalled {i} / {len(numbers)} values')
                return


    def digitSpanOrdered(self, drill):
        printBar(drill)
        numbers = self.getSequences()
        for i, value in enumerate(numbers):
            self.displayValue(value)
            correct = self.quiz(digit=''.join(sorted(value)))
            if not correct:
                print(f'You correctly recalled {i} / {len(numbers)} values')
                return
