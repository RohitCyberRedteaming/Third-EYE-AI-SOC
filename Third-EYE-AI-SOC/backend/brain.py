from backend.modules.threat_intel import check_virustotal
from backend.modules.mitre_mapper import map_mitre
from backend.modules.compliance import check_compliance
from backend.modules.ueba import detect_anomaly

def analyze_offense(off):
    ip = off.get("source_address", "")
    user = off.get("username", "unknown")
    desc = off.get("description", "")
    magnitude = off.get("magnitude", 0)

    vt = check_virustotal(ip)
    mitre = map_mitre(desc)
    compliance = check_compliance(desc)
    ueba = detect_anomaly([1,2,3,4,10])

    risk = (magnitude + vt) / 2

    decision = "IGNORE"
    if risk > 7:
        decision = "BLOCK"
    elif risk > 5:
        decision = "MONITOR"

    if ueba == "ANOMALY":
        decision = "ESCALATE"

    return {
        "ip": ip,
        "user": user,
        "decision": decision,
        "mitre": mitre,
        "risk": risk,
        "compliance": compliance
    }