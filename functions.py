# Colors
red = '\033[31m'
pink = '\033[35m'
rst = '\033[0m'


def deleteLine(nLines=1):
    print('\033[F\033[2K' * nLines, end='')  # Move cursor up & delete


def printBar(msg='', l=50):
    print('*' * l)
    if msg:
        print(msg)


def printError(msg):
    print(f'{red}{msg}{rst}')


def question(params):
    print('Select Exercise:')
    for k, v in params.items():
        print(f'  {k}: {v}')
    while True:
        x = input('Enter value: ')
        if x in params.keys():
            return params[x]
        else:
            deleteLine()


def query(prompt, dType):
    i = input(prompt)
    try:
        return dType(i)
    except:
        return False
