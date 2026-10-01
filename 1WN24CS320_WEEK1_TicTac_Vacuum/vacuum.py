import random
import time

class VacuumEnvironment:
    def __init__(self):
        # Possible statuses: "Clean" or "Dirty"
        self.locations = {
            "A": random.choice(["Clean", "Dirty"]),
            "B": random.choice(["Clean", "Dirty"])
        }
        # Randomly place the vacuum in room A or B
        self.agent_location = random.choice(["A", "B"])

    def get_percept(self):
        """Returns the current location and its cleanliness status."""
        return self.agent_location, self.locations[self.agent_location]

    def execute_action(self, action):
        """Updates the environment state based on the agent's action."""
        if action == "Suck":
            self.locations[self.agent_location] = "Clean"
        elif action == "MoveRight" and self.agent_location == "A":
            self.agent_location = "B"
        elif action == "MoveLeft" and self.agent_location == "B":
            self.agent_location = "A"

    def are_all_rooms_clean(self):
        """Checks if the performance goal is met."""
        return self.locations["A"] == "Clean" and self.locations["B"] == "Clean"


class SimpleReflexVacuumAgent:
    def __init__(self):
        pass

    def program(self, percept):
        """Condition-action rules: Decides what to do based on current perception."""
        location, status = percept
        
        if status == "Dirty":
            return "Suck"
        elif location == "A":
            return "MoveRight"
        elif location == "B":
            return "MoveLeft"


# --- Simulation Execution ---
if __name__ == "__main__":
    # Initialize the environment and the AI agent
    env = VacuumEnvironment()
    agent = SimpleReflexVacuumAgent()
    
    print("--- Starting Vacuum Cleaner Simulation ---")
    print(f"Initial State -> Room A: {env.locations['A']} | Room B: {env.locations['B']}")
    print(f"Vacuum starting location: Room {env.agent_location}\n")
    
    step = 1
    # Run the loop until both rooms are completely clean
    while not env.are_all_rooms_clean():
        print(f"--- Step {step} ---")
        
        # 1. Agent perceives the environment
        current_percept = env.get_percept()
        print(f"Perception: Location {current_percept[0]} is {current_percept[1]}")
        
        # 2. Agent decides on an action using its reflex program
        chosen_action = agent.program(current_percept)
        print(f"Action Determined: {chosen_action}")
        
        # 3. The action is executed, altering the environment
        env.execute_action(chosen_action)
        print(f"Current State -> Room A: {env.locations['A']} | Room B: {env.locations['B']}\n")
        
        step += 1
        time.sleep(1)  # Brief pause for human readability
        
    print("Goal Achieved: Both rooms are completely clean!")
