import statistics
def detect_anomaly(data):
    avg = statistics.mean(data)
    if data[-1] > avg*3:
        return "ANOMALY"
    return "NORMAL"