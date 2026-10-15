import itertools

def count_conflicts(board):
    """Calculate total pairs of attacking queens (heuristic h)."""
    conflicts = 0
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1
    return conflicts

def trace_swap_hill_climbing(start_board):
    current = list(start_board)
    current_h = count_conflicts(current)
    step = 0

    print("=== HILL CLIMBING WITH SWAPS (EARLY STOPPING AT h=0) ===")
    print(f"Start State: {current} | Heuristic h = {current_h}\n")

    # Check if initial state is already solved
    if current_h == 0:
        print(f"SUCCESS: Initial state {current} is already solved with h = 0!")
        return

    while True:
        print(f"--- STEP {step}: Current State = {current} (h = {current_h}) ---")
        
        swap_pairs = list(itertools.combinations(range(len(current)), 2))
        print(f"Evaluating up to {len(swap_pairs)} unique pairwise swap combinations:")

        best_neighbor = None
        best_h = current_h
        goal_found = False

        for idx, (i, j) in enumerate(swap_pairs, 1):
            neighbor = list(current)
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbor_h = count_conflicts(neighbor)

            print(f" Combination {idx}: Swap Col {i} & Col {j} -> State: {neighbor} | h = {neighbor_h}")

            # STOP IMMEDIATELY if goal state (h=0) is found
            if neighbor_h == 0:
                print(f"\n=> SUCCESS: Reached Goal State {neighbor} with h = 0! Stopping immediately.")
                goal_found = True
                break

            if neighbor_h < best_h:
                best_h = neighbor_h
                best_neighbor = neighbor

        if goal_found:
            break

        # Stop if stuck in a local minimum
        if best_neighbor is None or best_h >= current_h:
            print("\n-------------------------------------------")
            print(f"STUCK: Local minimum reached at {current} with h = {current_h}.")
            break

        print(f"\n=> Selected Best Neighbor: {best_neighbor} with h = {best_h}\n")
        current = best_neighbor
        current_h = best_h
        step += 1

if __name__ == "__main__":
    initial_state = [3, 1, 2, 0]
    trace_swap_hill_climbing(initial_state)