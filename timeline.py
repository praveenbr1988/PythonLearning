import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Data for milestones
milestones = [
    ("Level 3 Start", "Jan 2025"),
    ("Level 3 Finish", "Jun 2025"),
    ("Level 4 Start", "Jul 2025"),
    ("Level 4 Finish", "Dec 2025"),
    ("Level 5 Start", "Jan 2026"),
    ("Level 5 Finish", "Jun 2026"),
    ("Diploma Start", "Jan 2028"),
    ("Bachelor Start", "Jan 2029"),
    ("Bachelor Finish", "Dec 2030")
]

# Initialize plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, len(milestones))
ax.set_ylim(0, 1)
ax.axis('off')

# Plot function
def update(frame):
    ax.clear()
    ax.axis('off')
    for i in range(frame + 1):
        ax.text(i, 0.5, milestones[i][0], fontsize=12, ha='center')
        ax.text(i, 0.3, milestones[i][1], fontsize=10, ha='center')
    ax.plot(range(frame + 1), [0.5] * (frame + 1), marker="o", color="blue")

ani = FuncAnimation(fig, update, frames=len(milestones), interval=1000)

# Save animation
ani.save("piano_learning_timeline.gif", writer="pillow")
plt.show()
