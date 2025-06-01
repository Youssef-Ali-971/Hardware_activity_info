import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("system_log.csv")

# Convert timestamp column to datetime for accurate plotting
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Sort by timestamp to ensure proper chronological order
df = df.sort_values('timestamp')

# Create the plot
fig, ax = plt.subplots(figsize=(12, 6))

# Plot the data
ax.plot(df['timestamp'], df['cpu_percent'], label='CPU Usage (%)', linewidth=2)
ax.plot(df['timestamp'], df['memory_percent'], label='Memory Usage (%)', linewidth=2)

# Customize the plot
ax.set_title("CPU and Memory Usage Over Time", fontsize=14, fontweight='bold')
ax.set_xlabel("Timestamp", fontsize=12)
ax.set_ylabel("Usage (%)", fontsize=12)
ax.legend()
ax.grid(True, alpha=0.3)

# Format x-axis for better readability
plt.xticks(rotation=45)
fig.autofmt_xdate()  # Automatically format dates on x-axis

# Adjust layout and save
plt.tight_layout()
plt.savefig("metrics_plot.png", dpi=300, bbox_inches='tight')
print("Plot saved as metrics_plot.png")

# Display basic info about the data
print(f"Data range: {df['timestamp'].min()} to {df['timestamp'].max()}")
print(f"Total data points: {len(df)}")
