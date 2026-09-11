class Sensor:
    def __init__(self, id, name,temp, vibration):
        self.id = id
        self.name = name
        self.temp = temp
        self.vibration = vibration

    def print_info(self):
        print(self.name)
    def field_status_check(self):
        temp_status = "OK" if self.temp <= 30 else "WARNING, HIGH TEMPERATURE"
        vibration_status = "OK" if self.vibration <= 3.0 else "WARNING, HIGH VIBRATION"
        
        return[f"TEMPERATURE STATUS: {temp_status}", f"VIBRATION STATUS: {vibration_status}"]
       