import heapq

def h_manhattan(state, goal):
    """Calculates total Manhattan distance for all tiles to their goal positions."""
    distance = 0
    for i in range(9):
        val = state[i]
        if val != 0:
            target_idx = goal.index(val)
            r1, c1 = divmod(i, 3)
            r2, c2 = divmod(target_idx, 3)
            distance += abs(r1 - r2) + abs(c1 - c2)
    return distance

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
    initial_h = h_manhattan(start, goal)
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
                h = h_manhattan(neighbor, goal)
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