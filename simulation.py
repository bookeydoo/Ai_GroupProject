from classes import environment
from classes.gui import CleaningGUI 
import numpy

def main():
    # Define your grid size, initial agent position, and dirt locations
    grid_size = (5, 5)
    agent_start = (0, 0)
    dirt_positions = [(1, 1), (3, 2), (4, 4)]

    # Create the GUI object
    gui = CleaningGUI(grid_size=grid_size, dirt_positions=dirt_positions, agent_pos=agent_start)

    # Define the agent's planned steps (row, col)
    agent_steps = [
        (0,0), (0,1), (1,1), (2,1),
        (3,2), (4,2), (4,3), (4,4)
    ]
    gui.set_steps(agent_steps)

    # Start the GUI
    import matplotlib.pyplot as plt
    plt.show()  # This will display the GUI window

if __name__ == "__main__":
    main()