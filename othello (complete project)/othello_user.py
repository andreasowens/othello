#andres owens // 58449528 // ics 32 // project 4
import logic

def user_options() -> None:
    '''
    Function allows user to input information regarding starting
    state of game board including ROW, CLOUMN, TURN, SETUP, and
    WIN_METH.
    '''
    print("FULL")
    logic.ROW = int(input())
    logic.COLUMN = int(input())   
    logic.TURN = input()
    logic.SETUP = input()
    logic.WIN_METH = input()

def print_board(board:[[int]])  -> None:
    '''
    Function will allow program to print/display board for
    simplicity and visual usage by user as well as display
    score for both players. 
    '''
    for row in range(logic.ROW):
        for col in range(logic.COLUMN):
            if board[row][col] == logic.BLACK:
                print("B ", end="")
            elif board[row][col] == logic.WHITE:
                print("W ", end="")
            else :
                print(". ", end="")
        print()

def status_check(othello:logic.Othello_State)  -> None:
    '''
    Function will check status of current game and end game if
    list of valid user disc drops is empty for both users. Other-
    wise will continue to run game and change user turn.
    '''

    othello._disc_color_match()
    othello._validate_list()
    if othello._return_valid() != []:
        return True

    othello.rotate_turn()
    othello._disc_color_match()
    othello._valdate_list()
    if othello._return_valid() != []:
        return True

    return False
