
# Value Iteration in Grid World

import numpy as np

grid_size = 4
goal = (3, 3)
obstacle = (1, 1)

actions = {
    "UP": (-1, 0),
    "DOWN": (1, 0),
    "LEFT": (0, -1),
    "RIGHT": (0, 1)
}

gamma = 0.9
theta = 0.001

V = np.zeros((grid_size, grid_size))

def move(state, action):
    r, c = state
    dr, dc = actions[action]

    nr, nc = r + dr, c + dc

    if (nr < 0 or nr >= grid_size or
        nc < 0 or nc >= grid_size or
        (nr, nc) == obstacle):
        return state

    return (nr, nc)

# Value Iteration
while True:
    delta = 0

    for r in range(grid_size):
        for c in range(grid_size):
            state = (r, c)

            if state == goal or state == obstacle:
                continue

            old_value = V[r, c]
            values = []

            for action in actions:
                next_state = move(state, action)

                reward = 10 if next_state == goal else -1

                nr, nc = next_state
                values.append(reward + gamma * V[nr, nc])

            V[r, c] = max(values)
            delta = max(delta, abs(old_value - V[r, c]))

    if delta < theta:
        break

# Extract Optimal Policy
policy = {}

for r in range(grid_size):
    for c in range(grid_size):
        state = (r, c)

        if state == goal:
            policy[state] = "GOAL"
        elif state == obstacle:
            policy[state] = "BLOCK"
        else:
            best_action = None
            best_value = float("-inf")

            for action in actions:
                next_state = move(state, action)
                nr, nc = next_state

                reward = 10 if next_state == goal else -1
                value = reward + gamma * V[nr, nc]

                if value > best_value:
                    best_value = value
                    best_action = action

            policy[state] = best_action

print("Value Function:")
print(np.round(V, 2))

print("\nOptimal Policy:")

for r in range(grid_size):
    for c in range(grid_size):
        print(f"{policy[(r, c)]:7}", end=" ")
    print()
