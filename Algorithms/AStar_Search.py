import heapq


class Custom:
    def __init__(self, cost, state):
        self.cost = cost
        self.state = state

    def __lt__(self, another):
        return self.cost < another.cost


def find_path(initial, heuristic):
    discovered_nodes = 1
    visited_nodes = 1
    lst = []
    heapq.heapify(lst)
    visited = set()
    visited_with_cost = {}
    g = {}
    heapq.heappush(lst, Custom(0, initial))
    visited.add(str(initial))
    visited_with_cost[str(initial)] = 0
    g[initial] = 0
    while lst:
        visited_nodes += 1
        custom = heapq.heappop(lst)
        current = custom.state
        if current.is_over():
            return construct_path(current), discovered_nodes, visited_nodes

        for next_state in current.get_all_possible_states():
            new_str = str(next_state)
            new_cost = heuristic(next_state) + g[current] + 1
            if (new_str in visited and visited_with_cost[new_str] > new_cost) or new_str not in visited:
                next_state.parent = current
                visited_with_cost[new_str] = new_cost
                visited.add(new_str)
                heapq.heappush(lst, Custom(new_cost, next_state))
                g[next_state] = g[current] + 1
                discovered_nodes += 1
    return [], discovered_nodes, visited_nodes


def construct_path(init):
    path = []
    while init.parent is not None:
        path.append(init)
        init = init.parent
    path.reverse()
    return path
