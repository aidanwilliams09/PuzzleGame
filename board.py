class Board:

    def __init__(self, initial_state=None, moved = None, board_size = (2,3)):
        rows, cols = board_size
        # assert len(list(initial_state)) == rows*cols
        if initial_state is None:
            self.values = []
        else:
            self.values = initial_state
        self.rows = rows
        self.cols = cols
        self.moved = moved

    def __eq__(self, other):
        return self.values == other.values

    def __str__(self):
        return str(self.values)
    
    def __hash__(self):
        return hash(str(self))

    def _top_row(self):
        return range(self.cols)

    def _bottom_row(self):
        bottom_left = (self.rows - 1) * self.cols
        bottom_right = bottom_left + self.cols
        return range(bottom_left, bottom_right)

    def _left_col(self):
        return range(0, self.rows * self.cols, self.cols)

    def _right_col(self):
        return range(self.cols - 1, self.rows * self.cols, self.cols)

    def get_current(self):
        return self.values.index(0)

    # try to move empty square up
    def up(self):
        """
        if `up` is a valid move, return a new board position
        with the empty piece shifted up. 

        If `up` is invalid, raise an `IllegalMove`
        """
        pos = self.get_current()
        if pos in self._top_row():
            return None

        new_pos = pos - self.cols
        new_board = list(self.values)
        new_board[pos], new_board[new_pos] = new_board[new_pos], new_board[pos]
        return Board(initial_state=new_board, board_size=(self.rows, self.cols), moved=new_board[pos])

    # try to move empty square down
    def down(self):
        """
        if `down` is a valid move, return a new board position
        with the empty piece shifted down. 

        If `down` is invalid, raise an `IllegalMove`
        """
        pos = self.get_current()
        if pos in self._bottom_row():
            return None

        new_pos = pos + self.cols
        new_board = list(self.values)
        new_board[pos], new_board[new_pos] = new_board[new_pos], new_board[pos]
        return Board(new_board, board_size=(self.rows, self.cols), moved=new_board[pos])

    # try to move empty square left
    def left(self):
        """
        if `left` is a valid move, return a new board position
        with the empty piece shifted left. 

        If `left` is invalid, raise an `IllegalMove`
        """
        pos = self.get_current()
        if pos in self._left_col():
            return None

        new_pos = pos - 1
        new_board = list(self.values)
        new_board[pos], new_board[new_pos] = new_board[new_pos], new_board[pos]
        return Board(new_board, board_size=(self.rows, self.cols), moved=new_board[pos])

    # try to move empty square right
    def right(self):
        """
        if `right` is a valid move, return a new board position
        with the empty piece shifted right. 

        If `right` is invalid, raise an `IllegalMove`
        """
        pos = self.get_current()
        if pos in self._right_col():
            return None

        new_pos = pos + 1
        new_board = list(self.values)
        new_board[pos], new_board[new_pos] = new_board[new_pos], new_board[pos]
        return Board(new_board, board_size=(self.rows, self.cols), moved=new_board[pos])
    

    def getvalues(self):
        return self.values

        