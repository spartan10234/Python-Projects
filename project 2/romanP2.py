"""
Program: TODO
Author: Eduardo Roman
Description: TODO
"""
from match_graphics import *
from random import seed, shuffle

import random

def shuffle_cards():
    '''
    Generates a shuffled deck of cards. When done, cards[i][j] is the name of the card in
    row i and column j. It is a 5x5 grid comprised of 12 card pairs and one extra card.

    TODO: document the parameters and return value
    '''
    # seed the random number generator
    seed()

    random.shuffle(images)
    deck=[]
    len(images)
    for i in range(len(images)-1):
        deck.append(images[i])
        deck.append(images[i])
    deck.append(images[-1])
    random.shuffle(deck)

    # The idea of how to shuffle is the following:
    # shuffle the images
    # pick out 12 of the images (these are the ones that will be pairs)
    # pick out the remaining image (this is the one that will have no pair)
    # gather together 2 of each pair and the extra into a list
    # shuffle that list

    # use the list of these 25 shuffled cards to build a 5x5 array of cards
    # TODO: fix this code. It currently is a 5x5 array of nothing but one card
    cards = []
    count=0
    for i in range(5):
        row = []
        for j in range(5):
            item = deck[count]
            row.append(item)
            count += 1
        cards.append(row)
    return cards


def show_card(win, cards, i, j):
    '''
    Shows the card at row i and column j in the 5x5 grid in the window.

    TODO: document the parameters and return value
    '''
    CARD_HEIGHT = 125  # height of the card (matched the height of each image)
    CARD_WIDTH = 125  # width of the card (matches the width of each image)
    X = i*125+25  # margin on the left and right of the board
    Y= j*125+25

    top_left_point = Point(X, Y)
    bottom_right_point = Point(X + CARD_WIDTH, Y + CARD_HEIGHT)
    enclosing_rectangle = Rectangle(top_left_point, bottom_right_point)
    enclosing_rectangle.setOutline('Yellow')
    enclosing_rectangle.setWidth(5)
    enclosing_rectangle.setFill('LightGreen')
    enclosing_rectangle.draw(win)
    # Draw a rectangle with a yellow border of line width 5
    #  at the location associated with card (i,j)
    #  Ex: card (0,0) has upper-right corner (XMARGIN, YMARGIN) and
    #   lower-right corner (XMARGIN+CARD_HEIGHT, YMARGIN+CARD_WIDTH)
    card = Image(Point(X+62.5, Y+62.5), cards[j][i])
    card.draw(win)
    # Then, place the image for cards[i][j] at the center of the rectangle.
    return


def hide_card(win, cards, i, j):
    '''
    Takes the window and cards and hides the card at row i and column j.

    TODO: document the parameters and return value
    '''
    CARD_HEIGHT = 125  # height of the card (matched the height of each image)
    CARD_WIDTH = 125  # width of the card (matches the width of each image)
    X = i * 125 + 25  # margin on the left and right of the board
    Y = j * 125 + 25

    top_left_point = Point(X, Y)
    bottom_right_point = Point(X + CARD_WIDTH, Y + CARD_HEIGHT)
    enclosing_rectangle = Rectangle(top_left_point, bottom_right_point)
    enclosing_rectangle.setOutline('Yellow')
    enclosing_rectangle.setWidth(5)
    enclosing_rectangle.setFill('LightGreen')
    enclosing_rectangle.draw(win)

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

    column_num = ((x - XMARGIN) // (CARD_WIDTH ))
    if (0<=column_num<=4):
        return column_num
    if x<XMARGIN or x>(BOARD_HEIGHT-XMARGIN):
        return -1





def get_row(y):
    '''
    Takes the y-coordinate and returns the row.
    If it it outside the board, returns -1.

    TODO: document the parameters and return value
    '''
    row_num = ((y- YMARGIN)//(CARD_HEIGHT))
    if (0<= row_num <= 4):
        return row_num
    if y<YMARGIN or y>(BOARD_WIDTH-YMARGIN):
        return -1





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
            hide_card(win, cards, i, j)

    # For Checkpoint B:
    # forever:
    # get a mouse click
    match_list= []
    clicks = 0
    while True:
        c_point = win.getMouse()
        x_point = c_point.getX()
        y_point = c_point.getY()
        row1= int(get_row(y_point))
        colm1= int(get_col(x_point))
        if row1==-1 or colm1==-1:
            continue
        print(row1, colm1)
        card_display= show_card(win, cards, colm1, row1)

        if clicks == 0:
            row2=row1
            colm2=colm1
        clicks+=1

        if clicks>=2:
            if row1== row2 and colm1==colm2:
                continue

            game_delay(1)
            print(cards[row1][colm1])
            print(cards[row2][colm2])

            if cards[row2][colm2]== cards[row1][colm1]:
                print('match')
                match_list.append(cards[row2][colm2])
                match_list.append(cards[row1][colm1])
            else:
                hide_card(win, cards,colm1,row1)
                hide_card(win,cards,colm2, row2)
            clicks=0











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

    win.close()

main()