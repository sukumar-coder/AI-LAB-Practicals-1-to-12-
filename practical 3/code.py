
import heapq

# Initial and Goal States
initial = (1, 2, 3,
           4, 0, 6,
           7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


# Heuristic 1: Misplaced Tiles
def misplaced_tiles(state):
    return sum(
        1 for i in range(9)
        if state[i] != 0 and state[i] != goal[i]
    )


# Heuristic 2: Manhattan Distance
def manhattan_distance(state):
    distance = 0

    for i in range(9):
        if state[i] != 0:
            current_row, current_col = divmod(i, 3)
            goal_index = goal.index(state[i])
            goal_row, goal_col = divmod(goal_index, 3)

            distance += (
                abs(current_row - goal_row)
                + abs(current_col - goal_col)
            )

    return distance


# Generate Possible Moves
def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    row, col = divmod(zero, 3)

    moves = [
        (-1, 0), (1, 0),
        (0, -1), (0, 1)
    ]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col

            new_state = list(state)
            new_state[zero], new_state[new_index] = (
                new_state[new_index], new_state[zero]
            )

            neighbors.append(tuple(new_state))

    return neighbors


# A* Search Algorithm
def a_star(start, heuristic):
    priority_queue = []
    heapq.heappush(
        priority_queue,
        (heuristic(start), 0, start, [start])
    )

    visited = {}
    expanded = 0

    while priority_queue:
        f, g, state, path = heapq.heappop(priority_queue)

        if state in visited and visited[state] <= g:
            continue

        visited[state] = g
        expanded += 1

        if state == goal:
            return path, g, expanded

        for neighbor in get_neighbors(state):
            new_g = g + 1

            if neighbor not in visited or new_g < visited[neighbor]:
                new_h = heuristic(neighbor)
                new_f = new_g + new_h

                heapq.heappush(
                    priority_queue,
                    (new_f, new_g, neighbor, path + [neighbor])
                )

    return None, -1, expanded


# Display Puzzle
def display_path(path):
    for step, state in enumerate(path):
        print("\nStep", step)

        for i in range(0, 9, 3):
            print(state[i:i+3])


# Main Program
heuristics = [
    ("Misplaced Tiles", misplaced_tiles),
    ("Manhattan Distance", manhattan_distance)
]

for name, heuristic in heuristics:
    print("\n==============================")
    print("Heuristic:", name)

    path, cost, expanded = a_star(initial, heuristic)

    if path:
        print("Path Cost:", cost)
        print("Nodes Expanded:", expanded)
        print("Total Steps:", len(path) - 1)
        display_path(path)
    else:
        print("No solution found")
