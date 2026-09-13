from functions import *
import numpy as np
import random
import readline
import sys


"""
    Master the fundamentals of mathematics by practicing the 
    multiplication & division tables, percentages, and fractions
"""


# Colors
red = '\033[31m'
cyan = '\033[36m'
pink = '\033[35m'
rst = '\033[0m'


class Math:
    def __init__(self, maxValue, randomize):
        self.maxValue = maxValue
        if self.maxValue <= 3: # Inspections
            print(f'Max Value (-m / --maxvalue) cannot be ≤ 3\n'
                  f'Resetting to 4')
            self.maxValue = 4
        self.randomize = randomize
        self.games = {
            '0': 'Set Parameters',
            '1': 'Multiplication Tables',
            '2': 'Double Digit Multiplication',
            '3': 'Division Tables',
            '4': 'Percentages',
            '5': 'Fractions',
            'e': 'End Game',
            'q': 'Quit'
        }


    def run(self):
        printBar()
        while True:
            exercise = question(params=self.games)
            if exercise == 'Set Parameters':
                self.params()
            elif exercise == 'Multiplication Tables':
                self.multiplication(exercise)
            elif exercise == 'Double Digit Multiplication':
                self.multiplicationDoubleDigit(exercise)
            elif exercise == 'Division Tables':
                self.division(exercise)
            elif exercise == 'Percentages':
                self.percentages(exercise)
            elif exercise == 'Fractions':
                self.fractions(exercise)
            elif exercise == 'End Game':
                printBar()
                break
            else:
                sys.exit()


    def params(self):
        delLine = 5
        while True:
            params = {
                '0': 'Done',
                '1': f'Max Value: {cyan}{self.maxValue}{rst}',
                '2': f'Randomize Values: {cyan}{self.randomize}{rst}'
            }
            print('Change Parameter:')
            for k, v in params.items():
                print(f'  {k}: {v}')
            x = input('Select Option: ')
            if x in params.keys():
                if x == '0':
                    break
                elif x == '1':
                    v = getInput(f'Set a new Max Value (min=4): ', int)
                    if isinstance(v, int):
                        if v >= 4: # Max Value (-m / --maxvalue) cannot be < 4
                            self.maxValue = v
                    deleteLine()
                elif x == '2':
                    self.randomize = not self.randomize
                deleteLine(nLines=delLine)
            else:
                deleteLine(nLines=delLine)


    @staticmethod
    def getValues(problemSet, maxValue):
        a, b = [], []
        if problemSet == 'multiplication' or problemSet == 'division':
            a = [v for v in range(3, maxValue + 1, 1) if v not in [10]]
            b = [v for v in range(3, 17, 1)]
        elif problemSet == 'double digits':
            v1 = random.randint(1, 9) * 10
            v2 = random.randint(1, 9)
            a.append(v1 + v2)
            b.append(v1 + v2)
            for _ in range(2):
                v2 = random.randint(1, 9)
                b.append(v1 + v2)
            for _ in range(2):
                v1 = random.randint(1, 9) * 10
                v2 = random.randint(1, 9)
                a.append(v1 + v2)
                b.append(v1 + v2)
            random.shuffle(b)
        elif problemSet == 'percentages':
            a = [v for v in range(100, maxValue, 50)]
            b = [v / 100 for v in range(10, 100, 10)]
        elif problemSet == 'fractions':
            a = [v for v in range(1, maxValue, 1)]
            b = [v / 100 for v in range(1, maxValue, 1)]
        # print(f'a: {a}\nb: {b}')
        return a, len(str(a[-1])), b, len(str(b[-1]))


    def multiplication(self, drill):
        printBar(drill)
        val, lenV, num, lenN = self.getValues(problemSet='multiplication',
                                              maxValue=self.maxValue)
        nRounds = len(val) - 1
        for r in range(1, nRounds + 1):
            # Select value
            i = random.randint(1, len(val) - 1)
            v = val[i]
            val = np.delete(val, i)
            spaceV = " " * (lenV - len(str(v)))
            print(f'\nValue: {pink}{v}{rst} ({r}/{nRounds})')
    
            # Test
            if self.randomize:
                random.shuffle(num)
            for n in num:
                value = v * n
                spaceN = " " * (lenN - len(str(n)))
                while True:
                    x = input(f'  {spaceV}{v} x {spaceN}{n} = ')
                    if x:
                        if float(x) == value:
                            break
                        else:
                            deleteLine()
                            printError(f'  {spaceV}{v} x {spaceN}{n} = {x}')
                    else:
                        deleteLine()
        printBar()


    def multiplicationDoubleDigit(self, drill):
        printBar(msg=drill)
        valA, lenA, valB, lenB = self.getValues(problemSet='double digits',
                                                maxValue=self.maxValue)
        nRounds = len(valA) - 1
        for r in range(1, nRounds + 1):
            # Select value
            i = random.randint(1, len(valA) - 1)
            vA = valA[i]
            valA = np.delete(valA, i)
            spaceA = " " * (lenA - len(str(vA)))
            print(f'\nValue: {pink}{vA}{rst} ({r}/{nRounds})')
    
            # Test
            for vB in valB:
                value = vA * vB
                if value == 1.0 or int(value) != value:
                    # print(f'* {d}, {n}, {value}')
                    continue
                spaceB = " " * (lenA - len(str(vB)))
                while True:
                    x = input(f'  {spaceA}{vA} * {vB}{spaceB} = ')
                    if x:
                        if float(x) == round(value, 2):
                            break
                        else:
                            deleteLine()
                            printError(f'  {spaceA}{vA} * {vB}{spaceB} = {x}')
                    else:
                        deleteLine()
        printBar()


    def division(self, drill):
        printBar(msg=drill)
        div, lenD, num, _ = self.getValues(problemSet='division', maxValue=self.maxValue)
        nRounds = len(div) - 1
        for r in range(1, nRounds + 1):
            # Select value
            i = random.randint(1, len(div) - 1)
            d = div[i]
            div = np.delete(div, i)
            spaceD = " " * (lenD - len(str(d)))
            print(f'\nValue: {pink}{d}{rst} ({r}/{nRounds})')
    
            # Determine values
            if self.randomize:
                random.shuffle(num)
            values = [d * n for n in num]
            lenN = len(str(values[-1]))
    
            # Test
            for n in values:
                value = n / d
                if value == 1.0 or int(value) != value:
                    # print(f'* {d}, {n}, {value}')
                    continue
                spaceN = " " * (lenN - len(str(n)))
                while True:
                    x = input(f'  {spaceN}{n} / {d}{spaceD} = ')
                    if x:
                        if float(x) == round(value, 2):
                            break
                        else:
                            deleteLine()
                            printError(f'  {spaceN}{n} / {d}{spaceD} = {x}')
                    else:
                        deleteLine()
        printBar()


    def percentages(self, drill):
        printBar(msg=drill)
        val, _, per, _ = self.getValues(problemSet='percentages', maxValue=1000)
        nRounds = len(val) - 1
        for r in range(nRounds):
            # Select value
            i = random.randint(1, len(val) - 1)
            v = val[i]
            val = np.delete(val, i)
            print(f'\nValue: {pink}{v}{rst} ({r}/{nRounds})')
    
            # Determine values
            percents = [p for p in per if (v * p) % 1 == 0]
            # print(f'Per: {pink}{percents}{rst}')
            if self.randomize:
                random.shuffle(percents)
    
            # Test
            for p in percents:
                pInt = int(p * 100)
                value = v * p
                while True:
                    x = input(f'  {pInt}% of {v} = ')
                    if x:
                        if float(x) == round(value, 2):
                            break
                        else:
                            deleteLine()
                            printError(f'  {pInt}% of {v} = {x}')
                    else:
                        deleteLine()


    def fractions(self, drill):
        printBar(msg=drill)
        val, lenV, div, lenD = self.getValues(problemSet='fractions', maxValue=10)
        nRounds = len(val) - 1
