# python_simulation/sim_tracker.py
import time
import random
import csv
import os

# Simulated data
def get_gps_data():
    lat = 12.9716 + random.uniform(-0.01, 0.01)
    lon = 77.5946 + random.uniform(-0.01, 0.01)
    return lat, lon

# Theft logic: detect if movement occurs outside a set radius
def check_theft(lat, lon):
    base_lat, base_lon = 12.9716, 77.5946
    if abs(lat - base_lat) > 0.005 or abs(lon - base_lon) > 0.005:
        return True
    return False

def run_simulation():
    if not os.path.exists('data'): os.makedirs('data')
    with open('data/sensor_logs.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Timestamp', 'Lat', 'Lon', 'Status', 'Alert'])
        
        for _ in range(10):
            lat, lon = get_gps_data()
            theft = check_theft(lat, lon)
            status = "STOLEN" if theft else "SAFE"
            alert = "!!! THEFT ALERT !!!" if theft else "NORMAL"
            
            print(f"[{status}] Lat: {lat:.4f}, Lon: {lon:.4f} - {alert}")
            writer.writerow([time.ctime(), lat, lon, status, alert])
            time.sleep(1)

if __name__ == "__main__":
    run_simulation()