import heapq

def h_misplaced(state, goal):
    """Counts the number of misplaced tiles (excluding the blank space '0')."""
    return sum(1 for i in range(9) if state[i] != 0 and state[i] != goal[i])

def get_neighbors(state):
    """Generates all valid next states by moving the blank space (0)."""
    neighbors = []
    zero_idx = state.index(0)
    row, col = divmod(zero_idx, 3)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    for dr, dc in moves:
        nr, nc = row + dr, col + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_zero_idx = nr * 3 + nc
            new_state = list(state)
            new_state[zero_idx], new_state[new_zero_idx] = new_state[new_zero_idx], new_state[zero_idx]
            neighbors.append(tuple(new_state))

    return neighbors

def a_star_search(start, goal):
    initial_h = h_misplaced(start, goal)
    pq = [(initial_h, 0, start, [start])]
    visited = {start: 0}

    while pq:
        f, g, current, path = heapq.heappop(pq)

        if current == goal:
            return path, g

        for neighbor in get_neighbors(current):
            new_g = g + 1
            if neighbor not in visited or new_g < visited[neighbor]:
                visited[neighbor] = new_g
                h = h_misplaced(neighbor, goal)
                f = new_g + h
                heapq.heappush(pq, (f, new_g, neighbor, path + [neighbor]))

    return None, float('inf')

def print_grid(state):
    for i in range(0, 9, 3):
        print(f" {state[i]} {state[i+1]} {state[i+2]} ")
    print()

if __name__ == "__main__":
    start_state = (1, 5, 2, 4, 8, 3, 0, 7, 6)
    goal_state  = (1, 2, 3, 4, 5, 6, 7, 8, 0)

    print("Initial State:")
    print_grid(start_state)

    print("Goal State:")
    print_grid(goal_state)

    path, cost = a_star_search(start_state, goal_state)
    print(f"Total depth (g): {cost}")
    print(f"Total steps taken: {len(path) - 1}\n")

    print("Step-by-step Solution Path:")
    for step, state in enumerate(path):
        print(f"Step {step}:")
        print_grid(state)