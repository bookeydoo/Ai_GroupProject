import matplotlib.pyplot as plt
#import matplotlib.patches as patches
#from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button, Slider
import numpy as np
import time


class CleaningGUI:
    def __init__(self,Env,Agent,title):
        self.Env= Env
        self.Agent=Agent
        self.running=False    
        self.Title=title
        plt.rcParams['toolbar'] = 'none' 
        

        #init figures
        self.Env.fig , self.Env.ax=plt.subplots()
        plt.subplots_adjust(bottom=0.2)
        plt.ion()
        self.render()

        #ADD BUTTONS
        self.start_ax = plt.axes([0.1, 0.05, 0.25, 0.1])
        self.reset_ax = plt.axes([0.6, 0.05, 0.25, 0.1])

        self.start_button = Button(self.start_ax, "Stop")
        self.reset_button = Button(self.reset_ax, "Reset")

        self.start_button.on_clicked(self.shutdown)
        self.reset_button.on_clicked(self.reset_simulation)
    
        # SPEED SLIDER
        self.speed_ax = plt.axes([0.1, 0.01, 0.8, 0.03])  
        self.speed_slider = Slider(
        self.speed_ax,
        "Time",
        valmin=0.05,    # fastest
        valmax=1.0,     # slowest
        valinit=0.2,    # default
        valstep=0.01
        )
        
        self.speed = 0.3
        self.speed_slider.on_changed(self.update_speed)

    
    def update_speed(self, val): 
            self.speed = val


    def shutdown(self, event):
        """When the user presses Start."""
        self.running = False 

    def reset_simulation(self, event):
        """Reset world, agent, score, dirt, steps."""
        self.running = True 
        self.Env.__init__(self.Env.size, dirt_count=5)   # reinitialize env
        self.Agent.actions_log = []
        self.render()

    def step(self):
        """Execute 1 step only if running=True"""
        if self.running:
            self.Agent.act()
            # If there is no dirt left in the environment, stop the simulation
            if not np.any(self.Env.grid == 1):
                self.running = False
            
            time.sleep(self.speed) #control speed
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

        Env.fig.canvas.manager.set_window_title(self.Title)
        Env.fig.canvas.draw()
        Env.fig.canvas.flush_events()


    
