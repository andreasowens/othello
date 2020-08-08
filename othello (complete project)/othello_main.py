#andres owens // 58449528 // ics 32 // project 4
import logic
import othello_user

if __name__ == "__main__":

    othello_user.user_options()
    othello = logic.Othello_State() 
    print('B: {}  W: {}'.format(othello.score_counter()[0], othello.score_counter()[1]))
    othello_user.print_board(othello.return_board())
    print("TURN:", othello.return_turn())          

    while othello_user.status_check(othello):
        
        othello.return_flip_list()

        drop = input().split()
        row = int(drop[0]) - 1
        column = int(drop[1]) - 1
        
        try:
            othello.disc_drop(row,column) 
            othello.rotate_turn() 
            print('VALID')
            
            print('B: {}  W: {}'.format(othello.score_counter()[0], othello.score_counter()[1]))#
            othello_user.print_board(othello.return_board())
            print("TURN:", othello.return_turn())
        except:
            print('INVALID')

    othello.winner_of_game()  
