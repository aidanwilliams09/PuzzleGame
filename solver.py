from state import State
import search

# traverse the nodes and return the path
def get_path(goal_pos):
    if goal_pos is None:
        return []

    if goal_pos.prev is None:
        return goal_pos.node
        
    pos = goal_pos.prev
    path = [goal_pos.node]

    while pos != None:
        path.append(pos.node)
        pos = pos.prev
    return path[::-1]


test_state = State(initial_state=[2, 0, 4, 1, 5, 3])
test_state2 = State(initial_state=[1, 3, 4, 2, 0, 5])
test_state3 = State(initial_state=[1, 4, 2, 5, 3, 0])

bfs_result = search.BFS(test_state3)
bfs_path = get_path(bfs_result)
print("BFS")
print("---------------------")
print([state.current.values for state in bfs_path])
print()

ucs_result = search.UCS(test_state3)
ucs_path = get_path(ucs_result)
print("UCS")
print("---------------------")
print([state.current.values for state in ucs_path])
print()

dfs_result = search.DFS(test_state3)
dfs_path = get_path(dfs_result)
print("DFS")
print("---------------------")
print([state.current.values for state in dfs_path])
print()

ids_result = search.IDS(test_state3)
ids_path = get_path(ids_result)
print("IDS")
print("---------------------")
print([state.current.values for state in ids_path])
print()