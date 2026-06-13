IoT Vehicle Tracking & Theft Prevention System

An industry-oriented IoT solution designed to provide real-time vehicle monitoring, geofencing, and automated theft prevention.
🚀 Project Overview

This system addresses the growing need for secure and efficient fleet management. By integrating edge-based sensors with a cloud-linked dashboard, the system provides real-time location data and triggers immediate alerts if a vehicle leaves a designated "safe zone."
🛠 Tech Stack

    Hardware Simulation: ESP32 (via Python-based simulation)

    Backend/Logic: Python

    Communication: MQTT (simulated via HiveMQ)

    Frontend: Streamlit

    Data Logging: CSV-based persistence

📂 Project Structure
Plaintext

IoT-Vehicle-Tracking-System/
├── assets/                  # Project screenshots & diagrams
├── arduino_code/            # ESP32 firmware for hardware deployment
├── python_simulation/       # Core logic & sensor data simulation
├── dashboard/               # Streamlit web-based UI
├── data/                    # Historical sensor logs
├── .gitignore               # Excludes sensitive files (venv, .env)
└── requirements.txt         # Project dependencies

⚙️ Setup Instructions

    Clone the repository:
    Bash

    git clone https://github.com/yourusername/IoT-Vehicle-Tracking-System.git
    cd IoT-Vehicle-Tracking-System

    Install dependencies:
    Bash

    pip install -r requirements.txt

    Run the Simulation (Terminal 1):
    Bash

    python python_simulation/sim_tracker.py

    Launch the Dashboard (Terminal 2):
    Bash

    streamlit run dashboard/app.py

📊 Key Features

    Real-time GPS Tracking: Continuous monitoring of vehicle coordinates.

    Geofencing: Automated alerts if the vehicle moves outside a pre-defined perimeter.

    Theft Prevention: Logic-based status updates (SAFE vs. STOLEN) with automated notification triggers.

🤝 Future Enhancements

    Integration with real GPS/GSM hardware modules (e.g., SIM800L).

    Deployment to cloud services (AWS/Heroku) for remote monitoring.

    Addition of a historical trip playback feature on an interactive map.
