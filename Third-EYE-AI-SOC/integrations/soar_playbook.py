from integrations.qradar_api import get_offenses
from backend.brain import analyze_offense
from integrations.firewall import block_ip

def run():
    for off in get_offenses():
        res = analyze_offense(off)
        if res["decision"] == "BLOCK":
            block_ip(res["ip"])
            print("BLOCK", res["ip"])

if __name__ == "__main__":
    run()