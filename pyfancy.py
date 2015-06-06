#!/usr/bin/python
# -*- coding: utf-8 -*-
# Pyfancy 0.9.6 by Cosmic Open Source Projects learn more at
# https://github.com/ilovecode1/pyfancy!

import sys  # Import SYS


def idleorcommandline():  # This is from Pylaunch API
    '''If idleorcommandline returns True its IDLE if False its command line!'''

    a = sys.executable
    m = '\\\\'
    m = m[0]
    while True:
        b = len(a)
        c = a[b - 1]
        if c == m:
            break
        a = a[:b - 1]
    if sys.executable == a + 'pythonw.exe':
        return True  # IDE
    else:
        return False  # CMD


get = idleorcommandline()

documentation = 'For help go to https://github.com/ilovecode1/pyfancy!'  # Docs


class pyfancy:  # Our Class

    if get:  # IDE

        # Remove Values in Varibles

        END = ''
        BLINK = ''
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
        BLACKTEXTGREYBACKGROUND = ''
    else:

         # It's ok to turn on varibles

        END = '\033[0m'
        BLINK = '\033[05m'
        BLACKTEXTGREYBACKGROUND = '\033[100m'
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

    def random():  # Random Collor

        from random import randint  # Get Random

        if get:  # Turn Off Varibles!

            return
        else:

             # Turn On Varibles

            BLINK = '\033[05m'
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

            rand = randint(1, 21)  # Random Varible

            # Set

            if rand == 1:

                return INVISABLE2

            if rand == 2:

                return PURPLEBLUE

            if rand == 3:

                return WHITETEXTBLACKBACKROUND

            if rand == 4:

                return MISTGREY

            if rand == 5:

                return PURPLE

            if rand == 6:

                return CYAN

            if rand == 7:

                return LIGHTGREY

            if rand == 8:

                return DARKGREY

            if rand == 9:

                return LIGHTRED

            if rand == 10:

                return LIGHTGREEN

            if rand == 11:

                return LIGHTBLUE

            if rand == 12:

                return PINK

            if rand == 13:

                return BLUE

            if rand == 14:

                return GREEN

            if rand == 15:

                return YELLOW

            if rand == 16:

                return RED

            if rand == 17:

                return BOLD

            if rand == 18:

                return UNDERLINE

            if rand == 19:

                return REVERSE

            if rand == 20:

                return STRIKETHROUGH

            if rand == 21:

                return INVISABLE


def demo():  # Quick Demo!
    print pyfancy.RED + 'HELLO RED!' + pyfancy.END
