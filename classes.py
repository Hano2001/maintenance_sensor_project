class Sensor:
    def __init__(self, id, name,temp, vibration,pressure):
        self.id = id
        self.name = name
        self.temp = temp
        self.vibration = vibration
        self.pressure = pressure

    def print_info(self):
        print(self.name)
    def field_status_check(self):
        temp_status = "OK" if self.temp <= 30 else "WARNING, HIGH TEMPERATURE"
        vibration_status = "OK" if self.vibration <= 3.0 else "WARNING, HIGH VIBRATION"
        if self.pressure < 5.0:
            pressure_status = "WARNING, LOW PRESSURE"
        elif self.pressure > 7.0:
            pressure_status = "WARNING, HIGH PRESSURE"
        else:
            pressure_status = "OK"
        
        return[f"TEMPERATURE STATUS: {temp_status}", f"VIBRATION STATUS: {vibration_status}", f"PRESSURE STATUS: {pressure_status}"]
       