from board import Board

class State:

    def __init__(self, initial_state=None, moved=None):
        self.current = Board(initial_state=initial_state or [], moved=moved)

    def __equ__(self, other):
        return self.current == other.current

    def __str__(self):
        return str(self.current)

    def __hash__(self):
        return hash(str(self))

    # try to move empty square up
    def up(self):
        up = self.current.up()
        if up is not None:
            return State(up)
        else:
            return None

    # try to move empty square down
    def down(self):
        down = self.current.down()
        if down is not None:
            return State(down)
        else:
            return None

    # try to move empty square left
    def left(self):
        left = self.current.left()
        if left is not None:
            return State(left)
        else:
            return None

    # try to move empty square right
    def right(self):
        right = self.current.right()
        if right is not None:
            return State(right)
        else:
            return None

    #return list of valid states
    def valid_successors(self):
        succ = []
        
        up = self.current.up()
        if up is not None:
            succ.append(State(up.values, up.moved))


        down = self.current.down()
        if down is not None:
            succ.append(State(down.values, down.moved))


        left = self.current.left()
        if left is not None:
            succ.append(State(left.values, left.moved))


        right = self.current.right()
        if right is not None:
            succ.append(State(right.values, right.moved))
        
        return succ
        