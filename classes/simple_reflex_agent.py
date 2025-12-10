import random
import time
from classes.environment import VacuumEnvironment


class SimpleReflexAgent:
    def __init__(self, environment):
        self.Env = environment
        self.actions_log = []

    def get_percept(self):
        return self.Env.get_percept()

    def choose_action(self):
        if self.get_percept() == "DIRTY":
            return "CLEAN"
        return random.choice(["UP", "DOWN", "LEFT", "RIGHT"])

    def act(self):

        action=self.choose_action()
        self.actions_log.append(action)

        # Apply action
        if action == "CLEAN":
            self.Env.clean()
        else:
            self.Env.move_agent(action)

        #self.Env.steps += 1
