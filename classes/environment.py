import random
import numpy as np


class VacuumEnvironment:
    def __init__(self, size=4, dirt_count=5):

        self.size = size
        self.grid = np.zeros((size, size), dtype=int)

        self.agent_pos = (0, 0)
        self.score = 0
        self.steps = 0

        self._place_random_dirt(dirt_count)


    def _place_random_dirt(self, amount):
        placed = 0
        while placed < amount:
            r = random.randint(0, self.size - 1)
            c = random.randint(0, self.size - 1)
            if self.grid[r][c] == 0:
                self.grid[r][c] = 1
                placed += 1


    def get_percept(self, pos=None):
        if pos is None:
            pos = self.agent_pos
        r, c = pos
        return "DIRTY" if self.grid[r][c] == 1 else "CLEAN"


    def is_dirty(self, pos=None):
        if pos is None:
            pos = self.agent_pos
        r, c = pos
        return self.grid[r][c] == 1

    def clean(self, pos=None):
        if pos is None:
            pos = self.agent_pos
        r, c = pos
        if self.grid[r][c] == 1:
            self.grid[r][c] = 0
            self.score += 10

    # ---------------------------------------------------
    def move_agent(self, action):
        r, c = self.agent_pos

        if action == "UP" and r > 0:
            r -= 1
        elif action == "DOWN" and r < self.size - 1:
            r += 1
        elif action == "LEFT" and c > 0:
            c -= 1
        elif action == "RIGHT" and c < self.size - 1:
            c += 1
        else:
            self.score -= 1

        self.agent_pos = (r, c)
        self.steps += 1

    # ---------------------------------------------------
   