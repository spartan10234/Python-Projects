"""
Program: CS 115 Project 3
Author: Eduardo Roman
Description: This program creates a
"""

from ghost_support import*
from graphics import *


def readfile(filename):
    try:
        infile = open(filename, "r")
        filetext = infile.read().splitlines()
        infile.close()
        new_list=[]
        count=1
        for text in filetext:
            count += 1
            if (text.isalpha())== True:
                new_list.append(text.lower())
        x= list(set(new_list))
        return x
    except FileNotFoundError:
        print('Error: Dictionary does not contain any/non-usable words!')
        sys.exit(-1)


def print_info(list):
    print('Nice Dictionary! Here is Some information about it.')
    print()
    print('Size of Dictionary:', len(list))
    print('Frequency of each letter:')
    import string
    for letter in string.ascii_uppercase:
        total=0
        for word in list:
            total+= (word.upper().count(letter))
        print(letter, ':',total, sep='')

def create_board():
    '''
    Generates the game window.
    :param: None
    :return: a graphics window
    '''
    window = GraphWin('Ghost Word Game', WINSIZE, WINSIZE)
    window.setBackground('gray')
    message = Text(Point(window.getWidth() / 2, 20), 'Welcome to a game of Ghost Word')
    #message.setFill("white")
    message.setSize(30)
    message.setStyle('italic')
    message.setOutline('cyan')
    message.draw(window)
    window.getMouse()
    window.close()
    return window

def generate_word(word):
    underscores_list= []
    for letter in word:
        underscores_list.append('_')
    print(word)
    print('\tHint: ', end='')
    for  blank in underscores_list:
        print( blank,'', end='')
    print()

    wrong_guesses=[]
    user_guess= (input('Guess: ')).lower()
    while True:
        for i in range (len(word)):
            if user_guess==(word[i]):
                underscores_list[i]=user_guess

        if user_guess.isalpha() != True or len(user_guess)>1:
            print('Please try again.', user_guess.upper(),'is not a valid guess.')

        elif user_guess not in word:
            wrong_guesses.append(user_guess.upper())
            print('Sorry,', user_guess.upper(), 'is not in the secret word.')
            print()
            print('\tHint: ', end='')
            for blank in underscores_list:
                print(blank, '', end='')
            print()
            print('\tNot in the Word: ', wrong_guesses)
            print('\tPossible words matching the pattern: ')
            print()
        else:
            print('Lucky you,', user_guess.upper(), 'is in the secret word!')
            print()
            print('\tHint: ', end='')
            for blank in underscores_list:
                print(blank, '', end='')
            print()
            print('\tNot in the Word: ', wrong_guesses)
            print('\tPossible words matching the pattern: ')
            print()
        user_guess= (input('Guess: ')).lower()


def main():

    ask_file= input('Enter a dictionary filename: ')
    print()
    file= readfile(ask_file)
    print_info(file)
    ask_user= input('Would you like to play a game of Ghost Word? Enter (yes or no): ')
    while ask_user.lower()!='n' or ask_user.lower()!='y':
        if ask_user.lower()=='n' or ask_user.lower()=='no':
            print('Have a super awesome day my friend!')
            sys.exit(-1)
        if ask_user.lower()=='y' or ask_user.lower()== 'yes':
            random_word = choose_word(file)
            generate_word(random_word)
            create_board()
        else:
            sys.exit(-1)
        print()
        ask_user = input('Would you like to play a game of Ghost Word? Enter (yes or no): ')



main()

