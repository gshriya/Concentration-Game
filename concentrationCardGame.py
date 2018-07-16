import random
from random import shuffle
def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    # YOUR CODE GOES HERE
    random.shuffle (deck)
    print("Shuffling the deck...\n")
    

def wait_for_player():
    '''()->None
    Pauses the program/game until the player presses enter
    '''
    input("\nPress enter to continue. ")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
   


def create_board(size):
    '''int->list of str
       Precondition: size is even positive integer between 2 and 52
       Returns a rigorous deck (i.e. board) of a given size.
    '''
    board = [None]*size 

    letter='A'
    for i in range(len(board)//2):
          board[i]=letter
          board[i+len(board)//2 ]=board[i]
          letter=chr(ord(letter)+1)
    return board

def print_board(a):
    '''(list of str)->None
       Prints the current board in a nicely formated way
    '''
    for i in range(len(a)):
        print('{0:4}'.format(a[i]), end=' ')
    print()
    for i in range(len(a)):
        print('{0:4}'.format(str(i+1)), end=' ')


def print_revealed(discovered, p1, p2, original_board):
    '''(list of str, int, int, list of str)->None
    Prints the current board with the two new positions (p1 & p2) revealed from the original board
    Preconditions: p1 & p2 must be integers ranging from 1 to the length of the board
    '''
    # YOUR CODE GOES HERE
    for i in range(len(original_board)):
        if i == p1 - 1 or i == p2 -1:
            print('{0:4}'.format(original_board[i]), end=' ')
        else:
            print('{0:4}'.format(discovered[i]), end=' ')

    print()

    for i in range(len(discovered)):
        print('{0:4}'.format(str(i + 1)), end=' ')
    

#############################################################################
#   FUNCTIONS FOR OPTION 1 (with the board being read from a given file)    #
#############################################################################

def read_raw_board(file):
    '''str->list of str
    Returns a list of strings represeniting a deck of cards that was stored in a file. 
    The deck may not necessarifly be playable
    '''
    raw_board = open(file).read().splitlines()
    for i in range(len(raw_board)):
        raw_board[i]=raw_board[i].strip()
    return raw_board


def clean_up_board(l):
    '''list of str->list of str

    The functions takes as input a list of strings representing a deck of cards. 
    It returns a new list containing the same cards as l except that
    one of each cards that appears odd number of times in l is removed
    and all the cards with a * on their face sides are removed
    '''
    print("\nRemoving one of each cards that appears odd number of times and removing all stars ...\n")
    playable_board=[]

    
       

    # YOUR CODE GOES HERE
    for i in l:
        if '*' in l:
            l.remove('*')
        if (l.count(i)%2!=0):
            l.remove(i)
    for i in l:
        if l.count(i)==1:
            l.remove(i)
    if len(l)==1:
        l=[]
    playable_board=l
    return playable_board


def is_rigorous(l):
    '''list of str->True or None
    Returns True if every element in the list appears exactlly 2 times or the list is empty.
    Otherwise, it returns False.

    Precondition: Every element in the list appears even number of times
    '''

    # YOUR CODE GOES HERE
    
    for i in range(len(l)):
        if l.count(l[i])!=2:
            return False 
            
    return True
                
        

####################################################################


# This function builds a masked board to represent the dull side
def build_board(board):

    masked_board = board[:]
    for i in range(len(masked_board)):
        masked_board[i] = '*';

    return masked_board


def play_game(board):
    '''(list of str)->None
    Plays a concentration game using the given board
    Precondition: board a list representing a playable deck
    '''
    wait_for_player()
    shuffle_deck(board)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    print("Ready to play ...\n")

    # this is the funciton that plays the game
    # YOUR CODE GOES HERE
    masked_board = build_board(board)

    print_board(masked_board)

    num1 = None
    num2 = None
    
    flag = True
    guesses = 0

    if (len(board))>0:
        while flag:
            print('\nEnter two distinct positions on the board that you want revealed.')
            print('i.e two integers in the range [1, %d]' % len(board) )
            num1 = input('Enter position 1:')
            num2 = input('Enter position 2:')
            num1 = int(num1)
            num2 = int(num2)
            guesses += 1

            # If both entered numbers are same or masked board has a face side then ask
            # the user to re-enter
            if num1 == num2 or masked_board[num1 - 1] != '*' or masked_board[num2 - 1] != '*':

                print('One or both of you chosen positions hsa already been paired.')
                print('You chose the same positions')
                print('Please try again. This guess did not count. Your current number of guesses is %d' % guesses)
                continue

            print_revealed(masked_board, num1, num2, board)
            wait_for_player()

            # If both num1 and num2 has the same character then
            # set the masked_board to that character.
            if board[num1 - 1] == board[num2 - 1]:
                masked_board[num1 - 1] = board[num1 - 1]
                masked_board[num2 - 1] = board[num2 - 1]

            print_board(masked_board)

            # Check if all the * are gone.
            if masked_board.count('*') == 0:
                print('\nCongratulations@ You completed the game with %d guesses. That is %d more than the best possible. ' % (guesses, len(board) / 2))
                flag = False
    else:
        print('The resulting board is empty.\nPlaying concentration game with an empty board is impossible.\nGood Bye')

# YOUR CODE FOR OPTION 2 GOES HERE

# This funciton is responsible for loading
# the deck from the file.
def load_file_option():
    print("You chose to load a deck of cards from a file")
    file = input('Enter the name of the file:')
    file = file.strip()
    board=read_raw_board(file)
    board=clean_up_board(board)
    if is_rigorous(board)==True:
        print('*******************************************************************')
        print('*                                                                 *')
        print('* __This deck is now playable and rigorous and it has ',len(board),' cards__ *')
        print('*                                                                 *')
        print('*******************************************************************\n')
        

    elif is_rigorous(board)==False:
        print('************************************************************************')
        print('*                                                                      *')
        print('* __This deck is now playable but not rigorous and it has ',len(board),' cards__ *')
        print('*                                                                      *')
        print('************************************************************************\n')
    wait_for_player()
    play_game(board)
        
        
    
# This function is reponsible for handling the 
# rigorous option and also validates the input
# based on the pre-conditions (0 <= input <= 52 and even )
def rigorous_option():
    print('You chose to have a rigorous deck generated for you\n')


    flag = False
    num_of_cards = None

    while not flag:
        print('How many cards do you want to play with?')
        print('Enter an even number between 0 and 52:')
        num_of_cards = input('')
        num_of_cards = int(num_of_cards)

        if num_of_cards >= 2 and num_of_cards <= 52 and num_of_cards % 2 == 0:
            flag = True

    board = create_board(num_of_cards)
    
    play_game(board)

# YOUR CODE TO GET A CHOICE 1 or CHOCE 2 from a player GOES HERE

# This function shows the main menu to select either 
# rigorous or file option.
def main_menu():
    print('*******************************************')
    print('*                                         *')
    print('* __Welcome to my Concencentration Game__ *')
    print('*                                         *')
    print('*******************************************\n')
    print('Would you like (enter 1 or 2 to indicate your choice):')
    print('(1) me to generate a rigorous deck of cards for you')
    print('(2) or, would you like me to read a deck from a file?')


    while True:
        opt = input('')
        opt = int(opt)

        if opt == 1:
            rigorous_option()
            break
        elif opt == 2:
            load_file_option()
            break
        else:
            print('%d is not existing option.Please try again.Enter 1 or 2 to indicate your choice' % opt)

#main
if __name__ == '__main__':
    main_menu()

    
