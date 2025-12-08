import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button, Slider
import numpy as np

class CleaningGUI:
    def __init__(self, grid_size=(5, 5), dirt_positions=None, agent_pos=(0, 0)):
        self.grid_size = grid_size
        self.agent_pos = agent_pos
        self.dirt_positions = dirt_positions if dirt_positions else [(1, 1), (3, 2), (4, 4)]
        self.fig, self.ax = plt.subplots()
        plt.subplots_adjust(bottom=0.2)  # Make room for buttons/slider
        self.speed = 500  # in milliseconds
        self.anim = None
        self.steps = []  # Agent steps for animation

        self._init_grid()
        self._init_widgets()

    def _init_grid(self):
        self.ax.clear()
        self.ax.set_xlim(0, self.grid_size[1])
        self.ax.set_ylim(0, self.grid_size[0])
        self.ax.set_xticks(np.arange(0, self.grid_size[1]+1, 1))
        self.ax.set_yticks(np.arange(0, self.grid_size[0]+1, 1))
        self.ax.set_xticklabels([])
        self.ax.set_yticklabels([])
        self.ax.grid(True)
        self.agent_patch = patches.Circle((self.agent_pos[1]+0.5, self.grid_size[0]-self.agent_pos[0]-0.5),
                                          0.3, color='blue')
        self.ax.add_patch(self.agent_patch)

        self.dirt_patches = []
        for dirt in self.dirt_positions:
            patch = patches.Circle((dirt[1]+0.5, self.grid_size[0]-dirt[0]-0.5),
                                   0.2, color='brown')
            self.ax.add_patch(patch)
            self.dirt_patches.append(patch)

    def _init_widgets(self):
        ax_start = plt.axes([0.1, 0.05, 0.1, 0.075])
        self.btn_start = Button(ax_start, 'Start')
        self.btn_start.on_clicked(self.start_animation)

        ax_reset = plt.axes([0.25, 0.05, 0.1, 0.075])
        self.btn_reset = Button(ax_reset, 'Reset')
        self.btn_reset.on_clicked(self.reset)

        ax_slider = plt.axes([0.45, 0.05, 0.3, 0.03])
        self.slider = Slider(ax_slider, 'Speed', 100, 2000, valinit=self.speed, valstep=100)
        self.slider.on_changed(self.update_speed)

    def update_speed(self, val):
        self.speed = self.slider.val
        if self.anim:
            self.anim.event_source.interval = self.speed

    def set_steps(self, steps):
        """Set the sequence of agent moves [(row, col), ...]"""
        self.steps = steps

    def animate_step(self, i):
        if i >= len(self.steps):
            return
        pos = self.steps[i]
        self.agent_patch.center = (pos[1]+0.5, self.grid_size[0]-pos[0]-0.5)

        # Clean dirt if present
        for j, dirt in enumerate(self.dirt_positions):
            if dirt == pos:
                self.dirt_patches[j].set_visible(False)

    def start_animation(self, event):
        if not self.steps:
            print("No steps defined for the agent!")
            return
        self.anim = FuncAnimation(self.fig, self.animate_step, frames=len(self.steps),
                                  interval=self.speed, repeat=False)
        plt.draw()

    def reset(self, event):
        self.agent_pos = (0, 0)
        for patch in self.dirt_patches:
            patch.set_visible(True)
        self.agent_patch.center = (self.agent_pos[1]+0.5, self.grid_size[0]-self.agent_pos[0]-0.5)
        if self.anim:
            self.anim.event_source.stop()
        plt.draw()

