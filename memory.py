import time

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
    def __init__(self, timer):
        self.maxLen = 10
        self.minLen = 4
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
        delLine = 7
        distance = 5
        while True:
            limUpper = self.maxLen - distance
            limLower = self.minLen + distance
            params = {
                '0': 'Done',
                '1': f'Maximum Length: {cyan}{self.maxLen}{rst}',
                '2': f'Minimum Length: {cyan}{self.minLen}{rst}',
                '3': f'Time Limit: {cyan}{self.timer}{rst}'
            }

            print('Change Parameter:')
            for k, v in params.items():
                print(f'  {k}: {v}')
            x = input('Select Option: ')
            if x in params.keys():
                if x == '0':
                    break
                elif x == '1':
                    v = query(f'Maximum Digit Length (min={limLower}): ', int)
                    if isinstance(v, int):
                        if v >= limLower:
                            self.maxLen = v
                elif x == '2':
                    v = query(f'Minimum Digit Length (max={limUpper}): ', int)
                    if isinstance(v, int):
                        if v <= limUpper:
                            self.minLen = v
                elif x == '3':
                    v = query(f'Set Time Limit (min=1): ', float)
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
        return values


    def displayValue(self, digit):
        for d in digit:
            print(f'{red}{d}{rst}')
            time.sleep(self.timer)
            deleteLine()


    @staticmethod
    def quiz(digit):
        wasCorrect = False
        while True:
            ans = input('What was the value: ')
            if ans:
                if ans == digit:
                    wasCorrect = True
                break
            else:
                deleteLine()
        return ans, wasCorrect


    def digitSpan(self, drill):
        printBar(drill)
        numbers = self.getSequences()
        for value in numbers:
            self.displayValue(value)
            answer, correct = self.quiz(value)
            if not correct:
                x = ''
                for i in range(len(value)):
                    try:
                        if value[i] != answer[i]:
                            x += f'{red}{answer[i]}{rst}'
                        else:
                            x += answer[i]
                    except:
                        continue
                print(f'Incorrect answer\n'
                      f'* Value: {value}\n'
                      f'* Answer: {x}\n')
                return

    def digitSpanRev(self, drill):
        printBar(drill)
        numbers = self.getSequences()
        for value in numbers:
            self.displayValue(value)


    def digitSpanOrdered(self, drill):
        printBar(drill)
        numbers = self.getSequences()
        for value in numbers:
            self.displayValue(value)
