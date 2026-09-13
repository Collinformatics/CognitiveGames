import time


# Colors
red = '\033[31m'
pink = '\033[35m'
rst = '\033[0m'


def countdown():
    for i in reversed(range(1, 4)):
        print(f'Starting in {i}')
        time.sleep(1)
        deleteLine()


def deleteLine(nLines=1):
    print('\033[F\033[2K' * nLines, end='')  # Move cursor up & delete


def getInput(prompt, dType):
    i = input(prompt)
    try:
        return dType(i)
    except:
        return False


def helpMe(instructions, drillType):
    bar = '-'*50 + '\n'
    print(bar)
    print(f'\t\t{drillType}\n')
    for k, v in instructions.items():
        print(f'***** {k} *****\n{v}\n')
    print(bar)


def printBar(msg='', l=50):
    print('*' * l)
    if msg:
        print(msg)


def printError(msg):
    print(f'{red}{msg}{rst}')


def question(params, rm=3):
    print('Select Exercise:')
    for k, v in params.items():
        print(f'  {k}: {v}')
    while True:
        x = input('Enter value: ')
        if x in params.keys():
            deleteLine(nLines=len(params.keys())+rm)
            return params[x]
        else:
            deleteLine()
