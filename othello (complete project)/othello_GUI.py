import tkinter
import othello_logic

COLOR = 'pink'
LEN = 50

class Othello_GUI:
    '''
    '''
    def __init__(self):
        
        self._color = COLOR
        self._window = tkinter.Tk()
        self.create_board()
        self.fill_board()
        self._initial_board()

        game = othello_logic.Othello_State()


    def create_board(self):
        '''
        '''
        self._canvas = []
        for row in range(othello_logic.ROW):
            self._canvas.append([])
            for col in range(othello_logic.COLUMN):
                self._canvas[-1].append(othello_logic.NONE)


    def fill_board(self):
        '''
        '''
        global COLOR
        for row in range(othello_logic.ROW):
            for col in range(othello_logic.COLUMN):
                temp_canvas = tkinter.Canvas(
                    master = self._window,
                    width = LEN,
                    height = LEN,
                    background = COLOR)
                temp_canvas.grid(row = row, column = col,
                                 padx = 0, pady = 0,
                                 sticky = tkinter.N + tkinter.S +
                                 tkinter.E + tkinter.W)
                
                temp_canvas.bind('<Button-1>', self._mouse)
                

                self._canvas[row][col] = temp_canvas


                self._window.rowconfigure(row, weight = 1)
                self._window.columnconfigure(col, weight = 1)


    def _mouse(self, event: tkinter.Event) -> None:
        '''
        '''
        for row in range(othello_logic.ROW):
            for col in range(othello_logic.COLUMN):
                if self._canvas[row][col] == event.widget:
                    print(row,col)

                    ###LOGIC_CALLS


    def _initial_board(self) -> None:
        '''
        Function sets up initial board according to fourth line of input
        by user
        '''
        if othello_logic.SETUP == 'B':
            top_left = self._canvas[int(othello_logic.ROW/2)-1][int(othello_logic.COLUMN/2)-1].create_oval(
                LEN*.25, LEN*.25, LEN*.75, LEN*.75,
                fill = 'black')
            bottom_right = self._canvas[int(othello_logic.ROW/2)][int(othello_logic.COLUMN/2)].create_oval(
                LEN*.25, LEN*.25, LEN*.75, LEN*.75,
                fill = 'black')
            top_right = self._canvas[int(othello_logic.ROW/2)-1][int(othello_logic.COLUMN/2)].create_oval(
                LEN*.25, LEN*.25, LEN*.75, LEN*.75,
                fill = 'white')
            bottom_left = self._canvas[int(othello_logic.ROW/2)][int(othello_logic.COLUMN/2)-1].create_oval(
                LEN*.25, LEN*.25, LEN*.75, LEN*.75,
                fill = 'white')
        else:
            top_left = self._canvas[int(othello_logic.ROW/2)-1][int(self._column/2)-1].create_oval(
                LEN*.25, LEN*.25, LEN*.75, LEN*.75,
                fill = 'white')
            bottom_right = self._canvas[int(othello_logic.ROW/2)][int(self._column/2)].create_oval(
                LEN*.25, LEN*.25, LEN*.75, LEN*.75,
                fill = 'white')
            top_right = self._canvas[int(othello_logic.ROW/2)-1][int(self._column/2)].create_oval(
                LEN*.25, LEN*.25, LEN*.75, LEN*.75,
                fill = 'black')
            bottom_left = self._canvas[int(othello_logic.ROW/2)][int(self._column/2)-1].create_oval(
                LEN*.25, LEN*.25, LEN*.75, LEN*.75,
                fill = 'black')








##                if COLOR == 'white':
##                    COLOR = 'pink'
##                else:
##                    COLOR = 'white'
##            if COLOR == 'white':
##                COLOR = 'pink'
##            else:
##                COLOR = 'white'
                    

























