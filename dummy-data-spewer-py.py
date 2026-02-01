import time
import requests
import json
import random

SENSOR_ID = "STACJA_PZ_001"  
SERVER_URL = "http://twoj-serwer.com/api/dane"
INTERVAL = 30  
TIMEOUT = 5  

def pobierz_dane_z_czujnikow():
    """
    Symulacja odczytu pełnego zestawu parametrów.
    """
    return {
        "sensor_id": SENSOR_ID,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "smog_pm25": round(random.uniform(5, 35), 2),
        "smog_pm10": round(random.uniform(10, 50), 2),
        "wilgotnosc": round(random.uniform(40, 60), 1),
        "co2": random.randint(400, 1000),
        "cisnienie": round(random.uniform(980, 1030), 1),
        "temperatura": round(random.uniform(15, 22), 1)
    }

def main():
    print(f"--- URUCHOMIONO MONITORING ({SENSOR_ID}) ---")
    print(f"Interwał: {INTERVAL}s | URL: {SERVER_URL}\n")

    while True:
        dane = pobierz_dane_z_czujnikow()
        
        try:
            odpowiedz = requests.post(SERVER_URL, json=dane, timeout=TIMEOUT)
            odpowiedz.raise_for_status()
            
            print(f"[{dane['timestamp']}] Połączenie OK. Dane wysłane.")

        except (requests.exceptions.RequestException, Exception) as e:
            # Server does not respond, dump info to console
            print(f"\n" + "_"*40)
            print(f"[{dane['timestamp']}] BŁĄD POŁĄCZENIA!")
            print(f"Komunikat: {e}")
            print("DANE LOKALNE (JSON):")
            print(json.dumps(dane, indent=4, ensure_ascii=False))
            print("_"*40 + "\n")

        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()