# visualize_data.py
#
# Plots temperature data for each rack, marks overheat threshold,
# and saves the graph as an image (rack_temps.png).
#
# Run after generating data with generate_data.py.

import pandas as pd
import matplotlib.pyplot as plt

# Load the simulated data
df = pd.read_csv("simulated_env_log.csv")

plt.figure(figsize=(10, 6))  # Nice wide chart

# Plot temperature for each rack
for rack in df['rack'].unique():
    rack_data = df[df['rack'] == rack]
    plt.plot(
        rack_data['timestamp'], 
        rack_data['temperature_C'], 
        label=rack, 
        marker='o', 
        alpha=0.7
    )

# Draw the overheat line (e.g., 28°C)
plt.axhline(28, color='red', linestyle='--', label='Overheat threshold')

# Chart details
plt.title("Rack Temperatures Over 24 Hours")
plt.xlabel("Timestamp")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)  # Makes timestamps readable
plt.legend()
plt.tight_layout()  # Adjust spacing

# Save plot as image before showing (order matters!)
plt.savefig("rack_temps.png", dpi=150)
print("\nPlot saved as 'rack_temps.png' in your project folder.")

# Still show the chart window for quick look
plt.show()
