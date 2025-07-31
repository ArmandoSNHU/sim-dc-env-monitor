# generate_data.py
#
# Simulated Data Center Environmental Monitor
# Generates fake temperature/humidity data for a set of racks
#
# Run this first! It creates a CSV log for analysis/visualization.

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Configuration section (edit as needed)
NUM_RACKS = 5
HOURS = 24
START_TIME = datetime.now().replace(minute=0, second=0, microsecond=0)

data = []

for rack in range(1, NUM_RACKS + 1):
    temp = random.uniform(20, 24)  # initial temp
    hum = random.uniform(40, 50)   # initial humidity
    for h in range(HOURS):
        # Let temps/humidity drift for realism
        temp += np.random.normal(0, 0.8)
        hum += np.random.normal(0, 1.5)
        # 1-in-20 chance of a hot event
        if random.random() < 0.05:
            temp += random.uniform(5, 10)
        timestamp = START_TIME + timedelta(hours=h)
        data.append([
            timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            f"Rack-{rack}",
            round(temp, 2),
            round(hum, 2)
        ])

df = pd.DataFrame(data, columns=["timestamp", "rack", "temperature_C", "humidity_%"])
df.to_csv("simulated_env_log.csv", index=False)
print("\nSimulated sensor data written to simulated_env_log.csv")
print("You can now analyze or visualize this data.\n")
