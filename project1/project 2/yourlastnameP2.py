"""
Program: TODO
Author: TODO
Description: TODO
"""
from match_graphics import *
from random import seed, shuffle


def shuffle_cards():
    '''
    Generates a shuffled deck of cards. When done, cards[i][j] is the name of the card in
    row i and column j. It is a 5x5 grid comprised of 12 card pairs and one extra card.

    TODO: document the parameters and return value
    '''
    # seed the random number generator
    seed()

    # The idea of how to shuffle is the following:
    # shuffle the images
    # pick out 12 of the images (these are the ones that will be pairs)
    # pick out the remaining image (this is the one that will have no pair)
    # gather together 2 of each pair and the extra into a list
    # shuffle that list

    # use the list of these 25 shuffled cards to build a 5x5 array of cards
    # TODO: fix this code. It currently is a 5x5 array of nothing but one card
    cards = []
    for i in range(5):
        row = []
        for j in range(5):
            item = images[0]
            row.append(item)
        cards.append(row)
    return cards


def show_card(win, cards, i, j):
    '''
    Shows the card at row i and column j in the 5x5 grid in the window.

    TODO: document the parameters and return value
    '''

    # Draw a rectangle with a yellow border of line width 5
    #  at the location associated with card (i,j)
    #  Ex: card (0,0) has upper-right corner (XMARGIN, YMARGIN) and
    #   lower-right corner (XMARGIN+CARD_HEIGHT, YMARGIN+CARD_WIDTH)

    # Then, place the image for cards[i][j] at the center of the rectangle.
    return


def hide_card(win, cards, i, j):
    '''
    Takes the window and cards and hides the card at row i and column j.

    TODO: document the parameters and return value
    '''
    return


def mark_card(win, cards, i, j):
    '''
    Takes the window and cards and marks the card at row i and column j with a red X.

    TODO: document the parameters and return value
    '''
    return


def get_col(x):
    '''
    Takes the x-coordinate and returns the column.
    It the x coordinate is outside the board, returns -1.

    TODO: document the parameters and return value
    '''
    return 0


def get_row(y):
    '''
    Takes the y-coordinate and returns the row.
    If it it outside the board, returns -1.

    TODO: document the parameters and return value
    '''
    return 0



def main():
    '''
    TODO: describe how your main function works.
    '''

    # generate game window
    win = create_board()

    # shuffle the cards
    cards = shuffle_cards()

    # For Checkpoint A:
    # place all the cards, face-up
    for i in range(5):
        for j in range(5):
            show_card(win, cards, i, j)

    # For Checkpoint B:
    # forever:
        # get a mouse click
        # figure out which card was clicked
        # if this is a 'first pick':
            # show the card
        # else, if this is a 'second pick':
            # show the card
            # wait 1 second
            # if we have a 'matched pair':
                # mark both pairs as matched (Final Code)
            # else:
                # hide both cards
            # if we just won:
                # call the you_won function.
    win.getMouse()

main()