import csv
import random

# Define bounding box for Notre Dame campus
MIN_LAT, MAX_LAT = 41.695, 41.707
MIN_LNG, MAX_LNG = -86.245, -86.225

# Number of data points to generate
NUM_POINTS = 1000

# Output file
OUTPUT_FILE = "wifi_data.csv"

# Function to generate random lat/lng and signal strength
def generate_wifi_data(num_points):
    data = []
    for _ in range(num_points):
        lat = random.uniform(MIN_LAT, MAX_LAT)
        lng = random.uniform(MIN_LNG, MAX_LNG)
        strength = random.gauss(mu=70, sigma=15)  # realistic signal strength
        strength = max(0, min(100, round(strength)))  # Clamp to 0–100%
        data.append((lat, lng, strength))
    return data

# Write to CSV
def write_csv(data, filename):
    with open(filename, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['lat', 'lng', 'strength'])
        writer.writerows(data)

# Main
if __name__ == "__main__":
    wifi_data = generate_wifi_data(NUM_POINTS)
    write_csv(wifi_data, OUTPUT_FILE)
    print(f"✅ Generated {NUM_POINTS} synthetic WiFi data points in {OUTPUT_FILE}")