# analyze_data.py
#
# Reads simulated_env_log.csv and prints out any overheat events

import pandas as pd

# Load the data
df = pd.read_csv("simulated_env_log.csv")

OVERHEAT_THRESHOLD = 28.0  # degrees Celsius

# Find any readings above the threshold
alerts = df[df["temperature_C"] > OVERHEAT_THRESHOLD]

if not alerts.empty:
    print("\n--- WARNING: Overheat events detected! ---\n")
    print(alerts[["timestamp", "rack", "temperature_C"]])
    print(f"\nTotal overheat events: {len(alerts)}\n")
else:
    print("\nAll racks within normal temperature range.\n")
