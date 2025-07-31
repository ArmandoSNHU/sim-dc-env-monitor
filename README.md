# Simulated Data Center Environmental Monitor

This project simulates environmental monitoring in a data center, using Python to generate, analyze, and visualize temperature and humidity data for multiple server racks—no hardware required!

## Features

- **Data Simulation:** Generates realistic temperature and humidity data for several data center racks over a 24-hour period.
- **Anomaly Detection:** Scans the generated data to flag overheat events (e.g., racks exceeding a temperature threshold).
- **Visualization:** Plots temperature trends for each rack and saves the graph as a PNG image for reports or presentations.
- **Modular Scripts:** Each major task is its own script for easy understanding and reuse.

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/ArmandoSNHU/sim-dc-env-monitor.git
cd sim-dc-env-monitor
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Generate Simulated Data

```bash
python generate_data.py
```

### 4. Analyze for Overheat Events

```bash
python analyze_data.py
```

### 5. Visualize Temperatures

```bash
python visualize_data.py
```

The temperature graph will appear in a window and be saved as `rack_temps.png` in your project folder.

## File Overview

- `generate_data.py` — Generates fake sensor data and writes it to `simulated_env_log.csv`
- `analyze_data.py` — Flags racks with temperature over the threshold
- `visualize_data.py` — Plots and saves rack temperature trends as a PNG image
- `requirements.txt` — Lists needed Python packages

## Example Use Case

This project is great for:
- Practicing Python data analysis/visualization
- Demonstrating data center monitoring concepts without needing physical sensors
- Building a portfolio piece for IT, DevOps, or data engineering interviews

## License

MIT License (change if you need something else).

---

*Project by Armando. Contributions welcome!*
