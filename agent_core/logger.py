import csv
import os

LOG_FILE = 'logs/agent_history.csv'

def log_state(timestamp, state, confidence, message):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(['Timestamp', 'State', 'Confidence', 'Message'])
        writer.writerow([timestamp, state, confidence, message])
