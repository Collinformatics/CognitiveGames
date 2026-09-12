from functions import *
import numpy as np
import random
import readline
import sys

"""
    Improve your working memory with digit span games
"""

# Colors
red = '\033[31m'
cyan = '\033[36m'
pink = '\033[35m'
rst = '\033[0m'


class Memory:
    def __init__(self, nRuns, timer):
        self.nRuns = nRuns
        self.timer = timer
        self.games = {
            '0': 'Set Parameters',
            '1': 'Digit Span',
            '2': 'Digit Span Reversed',
            '3': 'Ordered Digit Span',
            'q': 'Quit'
        }


    def run(self):
        printBar()
        while True:
            exercise = question(params=self.games)
            if exercise == 'Set Parameters':
                self.params()
            if exercise == 'Digit Span':
                self.digitSpan(exercise)
            elif exercise == 'Digit Span Reversed':
                self.digitSpanRev(exercise)
            elif exercise == 'Ordered Digit Span':
                self.digitSpanRev(exercise)
            else:
                break


    def params(self):
        delLine = 6
        while True:
            params = {
                '0': 'Done',
                '1': f'Number of rounds: {cyan}{self.nRuns}{rst}',
                '2': f'Time Limit: {cyan}{self.timer}{rst}'
            }
            print('Change Parameter:')
            for k, v in params.items():
                print(f'  {k}: {v}')
            x = input('Select Option: ')
            if x in params.keys():
                if x == '0':
                    break
                elif x == '1':
                    v = query(f'Drill for N Rounds (min=1): ', int)
                    if isinstance(v, int):
                        if v > 0:
                            self.nRuns = v
                elif x == '2':
                    v = query(f'Set Time Limit (min=1): ', float)
                    if isinstance(v, float):
                        if v > 0:
                            self.timer = v
                deleteLine(nLines=delLine)
            else:
                deleteLine(nLines=delLine-1)


    def digitSpan(self, drill):
        printBar(drill)


    def digitSpanRev(self, drill):
        printBar(drill)


    def digitSpanOrdered(self, drill):
        printBar(drill)
