class ModelBasedAgent:
    def __init__(self, environment):
        self.Env = environment
        self.rows = environment.size
        self.cols = environment.size

        # Memory: -1 unknown, 0 clean, 1 dirty
        self.memory = [[-1 for _ in range(self.cols)] for _ in range(self.rows)]

        # Track visited tiles
        self.visited = set()

        self.actions_log = []

    def update_internal_state(self):
        r, c = self.Env.agent_pos
        dirty = self.Env.is_dirty()

        # Update memory
        self.memory[r][c] = 1 if dirty else 0
        self.visited.add((r, c))

        return r, c, dirty

    def act(self):
        r, c, dirty = self.update_internal_state()

        # Log perceptions
        if dirty:
            action = "CLEAN"
            self.actions_log.append(action)
            self.Env.clean()
            return

        # If memory shows a dirty tile, go to it
        target = self.find_dirty_tile()
        if target:
            action = self.move_towards(r, c, target)
            self.actions_log.append(action)
            self.Env.move_agent(action)
            return

        # Otherwise follow sweep pattern
        target = self.sweep_plan()
        action = self.move_towards(r, c, target)
        self.actions_log.append(action)
        self.Env.move_agent(action)

    def find_dirty_tile(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.memory[i][j] == 1:
                    return (i, j)
        return None

    def sweep_plan(self):
        for r in range(self.rows):
            if r % 2 == 0:
                col_range = range(self.cols)
            else:
                col_range = range(self.cols - 1, -1, -1)

            for c in col_range:
                if (r, c) not in self.visited:
                    return (r, c)
        return (0, 0)

    def move_towards(self, r, c, target):
        tr, tc = target
        if tr < r:
            return "UP"
        if tr > r:
            return "DOWN"
        if tc < c:
            return "LEFT"
        if tc > c:
            return "RIGHT"
        return "CLEAN"
