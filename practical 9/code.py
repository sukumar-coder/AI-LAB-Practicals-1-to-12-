
# Blocks World using Goal-Stack Planning

initial_state = {
    "ontable_A", "ontable_B",
    "clear_A", "clear_B",
    "handempty"
}

goal_state = {
    "on_A_B",
    "ontable_B",
    "clear_A",
    "handempty"
}

def apply_action(state, action):
    if action == "PICKUP_A":
        if "ontable_A" in state and "clear_A" in state and "handempty" in state:
            state.remove("ontable_A")
            state.remove("clear_A")
            state.remove("handempty")
            state.add("holding_A")
            return True

    elif action == "STACK_A_B":
        if "holding_A" in state and "clear_B" in state:
            state.remove("holding_A")
            state.remove("clear_B")
            state.add("on_A_B")
            state.add("clear_A")
            state.add("handempty")
            return True

    return False


state = initial_state.copy()
plan = ["PICKUP_A", "STACK_A_B"]

print("Initial State:")
print(sorted(state))

print("\nPlanning Actions:")

for action in plan:
    if apply_action(state, action):
        print("Action:", action)
        print("Current State:", sorted(state))

print("\nGoal State:")
print(sorted(goal_state))

if goal_state.issubset(state):
    print("\nGoal Achieved Successfully!")
else:
    print("\nGoal Not Achieved.")
