# Pyfancy 0.8 by Cosmic Open Source Projects learn more at
# https://github.com/ilovecode1/pyfancy

import sys


def idleorcommandline():
    'If idleorcommandline returns True its IDLE if False its command line!'
    a = sys.executable
    m = '\\\\'
    m = m[0]
    while True:
        b = len(a)
        c = a[(b - 1)]
        if c == m:
            break
        a = a[:(b - 1)]
    if sys.executable == a + 'pythonw.exe':
        return True
    else:
        return False

get = idleorcommandline()

documentation = (
    "Type documentation() for help or go to https://github.com/ilovecode1/pyfancy!")


def documentation(input=None):

    if (input is None):

        print(
            '''RANDOM\nprint (pyfancy.RANDOM + "Hello Random!" + pyfancy.END)\nBLUE\nprint (pyfancy.BLUE + "Hello Blue!" + pyfancy.END)\nGREEN\nprint (pyfancy.GREEN + "Hello Green!" + pyfancy.END)\nYELLOW\nprint (pyfancy.YELLOW + "Hello Yellow!" + pyfancy.END)\nRED\nprint (pyfancy.RED + "Hello Red!" + pyfancy.END)\nPINK\nprint (pyfancy.PINK + "Hello Pink!" + pyfancy.END)\nLIGHTBLUE\nprint (pyfancy.LIGHTBLUE + "Hello Lightblue!" + pyfancy.END)\nLIGHTGREEN\nprint (pyfancy.LIGHTGREEN + "Hello Lightgreen!" + pyfancy.END)\nLIGHTRED\nprint (pyfancy.LIGHTRED + "Hello Lightred!" + pyfancy.END)\nLIGHTGREY\nprint (pyfancy.LIGHTGREY + "Hello Lightgrey!" + pyfancy.END)\nDARKGREY\nprint (pyfancy.DARKGREY + "Hello Darkgrey!" + pyfancy.END)\nCYAN\nprint (pyfancy.CYAN + "Hello Cyan!" + pyfancy.END)\nPURPLE\nprint (pyfancy.PURPLE + "Hello Purple!" + pyfancy.END)\nBOLD\nprint (pyfancy.BOLD + "Hello Bold!" + pyfancy.END)\nUNDELINE\nprint (pyfancy.UNDERLINE + "Hello Underline!" + pyfancy.END)\nREVERSE\nprint (pyfancy.REVERSE + "Hello Reverse!" + pyfancy.END)\nSTRIKETHROUGH\nprint (pyfancy.STRIKETHOUGH + "Hello Strikethough!" + pyfancy.END)\nINVISABLE\nprint (pyfancy.INVISABLE + "Hello Invisable!" + pyfancy.END)''')

    else:

        print(input + " is not avalible!")


class pyfancy:

    if (get):

        END = ''
        INVISABLE2 = ''
        PURPLEBLUE = ''
        WHITETEXTBLACKBACKROUND = ''
        MISTGREY = ''
        PURPLE = ''
        CYAN = ''
        LIGHTGREY = ''
        DARKGREY = ''
        LIGHTRED = ''
        LIGHTGREEN = ''
        LIGHTBLUE = ''
        PINK = ''
        BLUE = ''
        GREEN = ''
        YELLOW = ''
        RED = ''
        BOLD = ''
        UNDERLINE = ''
        REVERSE = ''
        STRIKETHROUGH = ''
        INVISABLE = ''

    else:

        END = '\033[0m'
        INVISABLE2 = '\033[02m'
        PURPLEBLUE = '\033[34m'
        WHITETEXTBLACKBACKROUND = '\033[07m'
        MISTGREY = '\033[20m'
        PURPLE = '\033[35m'
        CYAN = '\033[36m'
        LIGHTGREY = '\033[37m'
        DARKGREY = '\033[90m'
        LIGHTRED = '\033[91m'
        LIGHTGREEN = '\033[92m'
        LIGHTBLUE = '\033[94m'
        PINK = '\033[95m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        REVERSE = '\033[07m'
        STRIKETHROUGH = '\033[09m'
        INVISABLE = '\033[08m'

    def random():

        from random import randint

        if (get):

            return

        else:

            INVISABLE2 = '\033[02m'
            PURPLEBLUE = '\033[34m'
            WHITETEXTBLACKBACKROUND = '\033[07m'
            MISTGREY = '\033[20m'
            PURPLE = '\033[35m'
            CYAN = '\033[36m'
            LIGHTGREY = '\033[37m'
            DARKGREY = '\033[90m'
            LIGHTRED = '\033[91m'
            LIGHTGREEN = '\033[92m'
            LIGHTBLUE = '\033[94m'
            PINK = '\033[95m'
            BLUE = '\033[94m'
            GREEN = '\033[92m'
            YELLOW = '\033[93m'
            RED = '\033[91m'
            BOLD = '\033[1m'
            UNDERLINE = '\033[4m'
            REVERSE = '\033[07m'
            STRIKETHROUGH = '\033[09m'
            INVISABLE = '\033[08m'

            rand = randint(1, 21)

            if (rand == 1):

                return INVISABLE2

            if (rand == 2):

                return PURPLEBLUE

            if (rand == 3):

                return WHITETEXTBLACKBACKROUND

            if (rand == 4):

                return MISTGREY

            if (rand == 5):

                return PURPLE

            if (rand == 6):

                return CYAN

            if (rand == 7):

                return LIGHTGREY

            if (rand == 8):

                return DARKGREY

            if (rand == 9):

                return LIGHTRED

            if (rand == 10):

                return LIGHTGREEN

            if (rand == 11):

                return LIGHTBLUE

            if (rand == 12):

                return PINK

            if (rand == 13):

                return BLUE

            if (rand == 14):

                return GREEN

            if (rand == 15):

                return YELLOW

            if (rand == 16):

                return RED

            if (rand == 17):

                return BOLD

            if (rand == 18):

                return UNDERLINE

            if (rand == 19):

                return REVERSE

            if (rand == 20):

                return STRIKETHROUGH

            if (rand == 21):

                return INVISABLE


def demo():
    print(pyfancy.RED + "HELLO RED!" + pyfancy.END)
