import json

filename = "sensors.json"
with open(filename) as jfile:
    sensor_data = json.load(jfile)