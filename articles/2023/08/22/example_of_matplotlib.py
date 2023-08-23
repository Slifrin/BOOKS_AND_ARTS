import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np


frequency_values = [1, 2, 3, 4]

t = np.linspace(0, 10, 1000)


fig, ax = plt.subplots(1, 1, figsize=(3.2, 2.4), dpi=300)

ax.set_facecolor("black")
ax.axis(False)
fig.set_facecolor("black")
line, = ax.plot(t, np.sin(frequency_values[0] * t), lw=5, color="white")
ax.set_ylim(-5, 5)

def animate(playhead):
    # print(playhead)
    # print(type(playhead))
    mask = t <= playhead
    line.set_data(t[mask], np.sin(4 * t[mask]))

anim = matplotlib.animation.FuncAnimation(fig, animate, t[::10], interval=30)

# anim.save("simple_animation.mp4")
plt.show()