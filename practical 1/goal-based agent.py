

class VacuumAgent:
    def __init__(self):
        self.location = "A"
        self.rooms = {
            "A": "Dirty",
            "B": "Dirty"
        }

    def perceive(self):
        return self.location, self.rooms[self.location]

    def act(self):
        location, status = self.perceive()

        if status == "Dirty":
            print(f"Room {location} is Dirty. Action: SUCK")
            self.rooms[location] = "Clean"

        elif location == "A":
            print("Room A is Clean. Action: MOVE RIGHT")
            self.location = "B"

        elif location == "B":
            print("Room B is Clean. Action: MOVE LEFT")
            self.location = "A"

    def goal_test(self):
        return all(status == "Clean"
                   for status in self.rooms.values())

    def run(self):
        print("Initial Environment:", self.rooms)
        print("\nAgent Execution:\n")

        while not self.goal_test():
            self.act()

        print("\nGoal Achieved!")
        print("Final Environment:", self.rooms)
        print("Both rooms are clean.")


# Create and run the agent
agent = VacuumAgent()
agent.run()
