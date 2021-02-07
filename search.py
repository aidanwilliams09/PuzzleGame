from collections import namedtuple
from operator import attrgetter


class PathError(Exception):
    pass


def is_goal_state(state):
    return str(state.current.values) == str([0, 1, 2, 5, 4, 3])


def BFS(cur_state):
    frontier = []
    Position = namedtuple('Position', 'node, prev')

    cur_pos = Position(cur_state, None)
    expanded = set()
    frontier.append(cur_pos)

    # loop until goal state is reached
    # if not goal state found, return None
    while len(frontier) != 0:

        pos = frontier.pop(0)
        state = pos.node
        
        if is_goal_state(state):
            return pos

        else:
            expanded.add(state)
            new_nodes = []
            # get next states and append to end of the frontier sorted by which piece is to be moved
            for a_state in state.valid_successors():

                in_frontier = a_state in [pos.node for pos in frontier]
                if a_state not in expanded and not in_frontier:
                    new_pos = Position(a_state, pos)
                    new_nodes.append(new_pos)
            
            if len(new_nodes) > 0:
                print([pos.node.current for pos in new_nodes])
                new_nodes = sorted(new_nodes, key=attrgetter('node.current.moved'))
                frontier.extend(new_nodes)

    return None


#BFS but includes total_cost in node to sort frontier with
def UCS(cur_state):
    frontier = []
    Position = namedtuple('Position', 'node, prev, total_cost')

    cur_pos = Position(cur_state, None, 0)
    expanded = set()
    frontier.append(cur_pos)

    while len(frontier) != 0:

        pos = frontier.pop(0)
        state = pos.node

        if is_goal_state(state):
            return pos

        else:
            expanded.add(state)
            for a_state in state.valid_successors():

                in_frontier = a_state in [pos.node for pos in frontier]
                if a_state not in expanded and not in_frontier:
                    new_pos = Position(a_state, pos, pos.total_cost + 1)
                    frontier.append(new_pos)
            
            frontier = sorted(frontier, key=attrgetter('total_cost'))

    return None

#depth limited search that is default capped at 50
def DFS(cur_state, depth_limit=50):
    frontier = []
    Position = namedtuple('Position', 'node, prev, total_cost')

    cur_pos = Position(cur_state, None, 0)
    expanded = set()
    frontier.append(cur_pos)

    while len(frontier) != 0:

        pos = frontier.pop(0)
        state = pos.node
        
        if is_goal_state(state):
            return pos
        
        else:
            expanded.add(state)
            for a_state in state.valid_successors():
            
                in_frontier = a_state in [pos.node for pos in frontier]
                if a_state not in expanded and not in_frontier and pos.total_cost < depth_limit:
                    new_pos = Position(a_state, pos, pos.total_cost + 1)
                    frontier.insert(0, new_pos)

    return None


# call DFS with increasing depth
def IDS(cur_state):
    depth = 0

    for depth in int_gen():
        
        end_node = DFS(cur_state, depth)
        if end_node is not None:
            return end_node

    return None

# helper generator for next depth
def int_gen():
    i = 0
    while True:
        yield i
        i += 1
