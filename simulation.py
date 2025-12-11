import time
import matplotlib.pyplot as plt

from classes.environment import VacuumEnvironment
from classes.simple_reflex_agent import SimpleReflexAgent
from classes.model_based_agent import ModelBasedAgent
from classes.gui import CleaningGUI


def run_simulation(agent_type, title):
    print(f"\n=== RUNNING {title} ===")

    env = VacuumEnvironment(size=5, dirt_count=5)
    agent = agent_type(env)
    gui = CleaningGUI(env, agent)

    gui.running = True  # start simulation automatically

    # Loop until simulation finishes
    while gui.running:
        gui.step()
        plt.pause(0.01)  # allow GUI events to process

    # Count clean tiles
    cleaned_tiles = sum(row.count(0) for row in env.grid.tolist())
    total_tiles = env.size * env.size
    dirty_tiles = total_tiles - cleaned_tiles

    print(f"\n=== REPORT: {title} ===")
    print("Score:", env.score)
    print("Steps:", env.steps)
    print("Remaining dirty tiles:", dirty_tiles)
    print("Clean tiles:", cleaned_tiles)
    print("----------------------------")

    # Close figure for this run
    plt.close(env.fig)


def main():
    # Run 1: Simple Reflex Agent
    run_simulation(SimpleReflexAgent, "Simple Reflex Agent")

    # Run 2: Model-Based Agent
    run_simulation(ModelBasedAgent, "Model-Based Agent")

    # Ensure all figures are closed at the end
    plt.close('all')
    print("\nSimulation finished.")
    # Optional: wait for user to see terminal report
    # input("Press Enter to exit...")


if __name__ == "__main__":
    main()
