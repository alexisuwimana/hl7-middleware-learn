import os
import json
from datetime import datetime


def save_message(hl7_msg):
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"logs/hl7_{now}.txt"
    with open(filename, 'w') as file:
        file.write(hl7_msg)
    print(f"📝 Saved HL7 to {filename}")


def save_parsed_data(parsed_json):
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"logs/parsed_{now}.json"
    with open(filename, 'w') as file:
        json.dump(parsed_json, file, indent=2)
    print(f"📝 Saved Parsed JSON to {filename}")
