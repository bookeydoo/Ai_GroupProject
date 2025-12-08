import random
import time
from environment import VacuumEnvironment


class SimpleReflexAgent:
    def __init__(self, environment):
        self.env = environment
        self.actions_log = []

    def get_percept(self):
        return self.env.get_percept()

    def choose_action(self):
        if self.get_percept() == "DIRTY":
            return "CLEAN"
        return random.choice(["UP", "DOWN", "LEFT", "RIGHT"])

    def step(self):
        action = self.choose_action()
        self.actions_log.append(action)

        if action == "CLEAN":
            self.env.clean()
        else:
            self.env.move_agent(action)

        self.env.render()
        time.sleep(0.3)

    def run(self, steps=20):
        for _ in range(steps):
            self.step()

        print("\n=== REFLEX AGENT REPORT ===")
        print("Score:", self.env.score)
        print("Steps:", self.env.steps)
        print("Actions:", self.actions_log)


if __name__ == "__main__":
    env = VacuumEnvironment(size=4, dirt_count=6)
    agent = SimpleReflexAgent(env)

    env.render()
    agent.run(steps=20)

    input("\nPress ENTER to exit...")
