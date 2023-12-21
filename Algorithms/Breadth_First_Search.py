def find_path(initial):
    discovered_nodes = 1
    visited_nodes = 1
    queue = []
    visited = set()
    queue.append((initial, []))
    visited.add(str(initial))

    while queue:
        visited_nodes += 1
        current, path = queue.pop(0)

        if current.is_over():
            return path, discovered_nodes, visited_nodes

        for next_state in current.get_all_possible_states():
            new_str = str(next_state)
            if new_str not in visited:
                next_state.parent = current
                visited.add(new_str)
                new_path = path + [next_state]
                queue.append((next_state, new_path))
                discovered_nodes += 1

    return [], discovered_nodes, visited_nodes
