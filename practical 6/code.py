
# CSP: Map Coloring Problem
# Backtracking with Consistency Checking

# Variables and Domains
variables = ['A', 'B', 'C', 'D', 'E']

colors = ['Red', 'Green', 'Blue']

# Adjacency constraints
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E'],
    'E': ['C', 'D']
}

# Store assigned colors
assignment = {}


# Check Consistency
def is_consistent(region, color):
    for neighbor in graph[region]:
        if neighbor in assignment:
            if assignment[neighbor] == color:
                return False

    return True


# Backtracking Algorithm
def backtracking():
    # Check if all variables are assigned
    if len(assignment) == len(variables):
        return True

    # Select an unassigned variable
    for region in variables:
        if region not in assignment:
            break

    # Try available colors
    for color in colors:

        if is_consistent(region, color):
            assignment[region] = color

            if backtracking():
                return True

            # Backtrack
            del assignment[region]

    return False


# Main Program
print("MAP COLORING PROBLEM")
print("--------------------")

if backtracking():
    print("\nSolution Found:\n")

    for region in variables:
        print(region, ":", assignment[region])

else:
    print("No solution exists.")
