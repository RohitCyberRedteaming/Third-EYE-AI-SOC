import requests
from backend.config import QRADAR_IP, QRADAR_TOKEN

def get_offenses():
    try:
        r = requests.get(f"{QRADAR_IP}/api/siem/offenses", headers={"SEC": QRADAR_TOKEN}, verify=False)
        return r.json()
    except:
        return []