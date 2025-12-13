import random

class ModelBasedAgent:
    def __init__(self, environment):
        self.Env = environment
        self.rows = environment.size
        self.cols = environment.size

        self.memory = [[-1 for _ in range(self.cols)] for _ in range(self.rows)]
        self.visited = set()
        self.actions_log = []

    def update_internal_state(self):
        r, c = self.Env.agent_pos
        dirty = self.Env.is_dirty()

        self.memory[r][c] = 1 if dirty else 0
        self.visited.add((r, c))

        return r, c, dirty

    def act(self):
        r, c, dirty = self.update_internal_state()

        # 1. Clean if dirty
        if dirty:
            self.actions_log.append("CLEAN")
            self.Env.clean()
            return

        # 2. Move toward any known dirty tile
        target = self.find_dirty_tile()
        if target:
            action = self.move_towards(r, c, target)
            self.actions_log.append(action)
            self.Env.move_agent(action)
            return

        # 3. Otherwise random model-based movement
        action = self.random_memory_move(r, c)
        self.actions_log.append(action)
        self.Env.move_agent(action)

    def find_dirty_tile(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.memory[i][j] == 1:
                    return (i, j)
        return None

    def random_memory_move(self, r, c):
        possible_moves = {
            "UP":    (r - 1, c),
            "DOWN":  (r + 1, c),
            "LEFT":  (r, c - 1),
            "RIGHT": (r, c + 1)
        }

        # 1. Only keep moves inside grid
        valid = [(action, pos) for action, pos in possible_moves.items()
                 if 0 <= pos[0] < self.rows and 0 <= pos[1] < self.cols]

        if not valid:
            return "UP"  # fallback, shouldn't happen

        # 2. Prefer unvisited tiles
        unvisited = [action for action, pos in valid if pos not in self.visited]
        if unvisited:
            return random.choice(unvisited)

        # 3. Otherwise choose ANY valid move
        return random.choice([action for action, pos in valid])

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