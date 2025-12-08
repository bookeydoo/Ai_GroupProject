from classes.environment import VacuumEnvironment
from classes.simple_reflex_agent import SimpleReflexAgent 
from classes.gui import CleaningGUI 
import matplotlib.pyplot as plt
import random
import time

def main():
    env = VacuumEnvironment(size=5, dirt_count=5)
    agent = SimpleReflexAgent(env)
    gui = CleaningGUI(env, agent)
    actions=[]
    plt.show(block=False)

    # Example sequence of actions (can also let agent choose automatically)
    for i in range(15):
        x=random.choice(["UP","DOWN","LEFT","RIGHT"])
        actions.append(x)

    for action in actions:
        gui.step(action)
        time.sleep(0.5)  # control speed

    print("\n=== FINAL REPORT ===")
    print("Score:", env.score)
    print("Steps:", env.steps)
    print("Actions:", agent.actions_log)

    plt.ioff()
    plt.show()  # keep window open

    input("\n Press enter to close")

if __name__ == "__main__":
    main()