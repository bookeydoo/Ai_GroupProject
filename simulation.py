from classes.environment import VacuumEnvironment
from classes.gui import CleaningGUI 
import matplotlib.pyplot as plt
import time

def main():
    env = VacuumEnvironment(size=5, dirt_count=5)
    gui = CleaningGUI(env)

    plt.show()
    plt.ioff()
    # Example sequence of actions
    actions = ["RIGHT", "RIGHT", "DOWN", "DOWN", "LEFT", "DOWN", "RIGHT", "RIGHT"]
    for action in actions:
        gui.step(action)
        time.sleep(1)  # control speed

    print(f"Final score: {env.score}, steps: {env.steps}")

if __name__ == "__main__":
    main()