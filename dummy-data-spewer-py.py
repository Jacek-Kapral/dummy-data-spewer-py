import time
import requests
import json
import random

SENSOR_ID = "STATION_PZ_001"  
SERVER_URL = "http://dummy-server-address.com/api/data"
INTERVAL = 30  
TIMEOUT = 5  

def get_sensor_data():
    """
    Full data set simulation.
    """
    return {
        "sensor_id": SENSOR_ID,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "pm25": round(random.uniform(5, 35), 2),
        "pm10": round(random.uniform(10, 50), 2),
        "humidity": round(random.uniform(40, 60), 1),
        "co2": random.randint(400, 1000),
        "pressure": round(random.uniform(980, 1030), 1),
        "temperature": round(random.uniform(15, 22), 1)
    }

def main():
    print(f"--- MONITORING STARTED ({SENSOR_ID}) ---")
    print(f"Time interval: {INTERVAL}s | URL: {SERVER_URL}\n")

    while True:
        dane = get_sensor_data()
        
        try:
            odpowiedz = requests.post(SERVER_URL, json=dane, timeout=TIMEOUT)
            odpowiedz.raise_for_status()
            
            print(f"[{dane['timestamp']}] Connection OK. Data sent.")

        except (requests.exceptions.RequestException, Exception) as e:
            # Server does not respond, dump info to console
            print(f"\n" + "_"*40)
            print(f"[{dane['timestamp']}] CONNECTION ERROR!")
            print(f"Error Message: {e}")
            print("LOCAL DATA (JSON):")
            print(json.dumps(dane, indent=4, ensure_ascii=False))
            print("_"*40 + "\n")

        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()