# Helper tools for the Attack Replay Framework

## `sync_events_to_db`

Reads SIEM events from a file and writes them to the DB buffer.  
To be used in conjunction with continuous mode of the Attack Replay Framework.  
SIEM events can be read in EVE JSON format as when exported directly from Splunk.  

### Usage
1. Install requirements from `requirements.txt`
1. Locate the JSON file with SIEM events
1. Load them into the buffer of the ARF DB: `python sync_events_to_db.py 127.0.0.1 27017 arf ~/events.json`

### Command line arguments:
```
python sync_events_to_db.py HOST PORT DB FILEPATH
```

where:
- `HOST`: The MongoDB host, should be a string containing the hostname or IP of the DB server. (Required)
- `PORT`: The MongoDB port, should be a string containing the port number of the DB server. (Required)
- `DB`: The MongoDB database name, should be a string containing the name of the DB. (Required)
- `FILEPATH`: The path to the JSON file, should be a string containing the file path of the JSON file. (Required)
