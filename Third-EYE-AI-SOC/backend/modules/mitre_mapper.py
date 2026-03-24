def map_mitre(desc):
    if "brute" in desc.lower():
        return "T1110"
    return "Unknown"