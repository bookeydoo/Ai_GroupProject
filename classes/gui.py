import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button, Slider
import numpy as np



class CleaningGUI:
    def __init__(self,Env,Agent):
        self.Env= Env
        self.Agent=Agent
        
        #init figures
        self.Env.fig , self.Env.ax=plt.subplots()
        plt.ion()
        self.render()

    def step(self, action=None):
        """Perform one agent step and update GUI"""
        self.Agent.act()
        self.render()
     

    def render(self):

        Env=self.Env
        Env.ax.clear()

        for i in range(Env.size + 1):
            Env.ax.axhline(i, color="black")
            Env.ax.axvline(i, color="black")

        # draw dirt
        for r in range(Env.size):
            for c in range(Env.size):
                if Env.grid[r][c] == 1:
                    Env.ax.plot(c + 0.5, Env.size - r - 0.5,
                                 "o", color="brown", markersize=28)

        # draw agent
        Arow, Acol = Env.agent_pos
        Env.ax.add_patch(plt.Rectangle(
            (Acol, Env.size - Arow- 1), 1, 1, color="skyblue"
        ))

        Env.ax.set_xlim(0, Env.size)
        Env.ax.set_ylim(0, Env.size)
        Env.ax.set_xticks([])
        Env.ax.set_yticks([])
        Env.ax.set_aspect("equal")

        Env.ax.set_title(f"Agent: {Env.agent_pos} | Score: {Env.score} | Steps: {Env.steps}")

        Env.fig.canvas.draw()
        Env.fig.canvas.flush_events()


    
