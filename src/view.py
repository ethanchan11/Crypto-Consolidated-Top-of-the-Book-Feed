import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import json

with open('config.json', 'r') as file:
    config = json.load(file)

# Constants
csv_file_path = config['output_file_path']

# Create figure for plotting
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 6))
plt.xticks(rotation=45, ha='right')

def animate(i):
    data = pd.read_csv(csv_file_path)

    x = data['time']
    y1 = data['bestbid']
    y2 = data['bestask']
    y3 = data['bestbidsize']
    y4 = data['bestasksize']

    # Limit x and y lists to 1000 items
    x = x[-1000:]
    y1 = y1[-1000:]
    y2 = y2[-1000:]
    y3 = y3[-1000:]
    y4 = y4[-1000:]

    # Draw x and y lists
    ax1.clear()
    ax1.plot(x, y1, label='best_bid')
    ax1.plot(x, y2, label='best_ask')
    ax1.legend(loc='upper left')
    ax1.set_title('ETHUSD Consolidated Quotes')
    ax1.set_ylabel('Price')

    ax2.clear()
    ax2.plot(x, y3, label='best_bid_size')
    ax2.plot(x, y4, label='best_ask_size')
    ax2.legend(loc='upper left')
    ax2.set_title('ETHUSD Consolidated Sizes')
    ax2.set_ylabel('Size')

    plt.tight_layout()

ani = animation.FuncAnimation(fig, animate, interval=1000, blit=False, save_count=100)
plt.tight_layout()
try:
    plt.show()
except KeyboardInterrupt:
    plt.close(fig)
