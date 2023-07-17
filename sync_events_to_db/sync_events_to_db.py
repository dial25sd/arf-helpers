import argparse
import json

from pymongo import MongoClient


# Unpack actual event content from Splunk event
def get_event_content(data: str) -> dict:
    if 'result' in data:
        if '_raw' in data.get('result'):
            return data.get('result')
    return data


parser = argparse.ArgumentParser(description='Read a JSON file containing SIEM events in EVE JSON format and save them to MongoDB.')
parser.add_argument('HOST', help='The MongoDB host (IP or hostname).')
parser.add_argument('PORT', help='The MongoDB port.')
parser.add_argument('DB', help='The MongoDB database name.')
parser.add_argument('FILEPATH', help='The path to the JSON file.')
args = parser.parse_args()

client = MongoClient(f'mongodb://{args.HOST}:{args.PORT}/')
db = client[args.DB]
events_collection = db['events']

# Load JSON data from file (either one valid JSON object/list or one valid JSON object per line)
with open(args.FILEPATH) as f:
    try:
        data = json.load(f)
    except json.decoder.JSONDecodeError as e:
        with open(args.FILEPATH) as f2:
            data = []
            for line in f2:
                try:
                    event = json.loads(line)
                    data.append(event)
                except json.decoder.JSONDecodeError as e:
                    print(e)
                    pass
    print(f"Read {len(data)} events.")

if not data:
    print("No data to insert!")
    exit(1)

if isinstance(data, list):
    data = [get_event_content(datum) for datum in data]
    events_collection.insert_many(data)
else:
    events_collection.insert_one(get_event_content(data))

print("Data inserted successfully.")
