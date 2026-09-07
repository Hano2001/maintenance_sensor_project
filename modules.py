def field_status_check(sensor):
    status_list = []
    for key, value in sensor.items():
        if key == "temperature":
            if value > 50:
              
                status_list.append("HIGH TEMPERATURE")
        elif key == "vibration":
            if value >= 6:
                status_list.append("HIGH VIBRATION")
        elif key == "pressure":
            if value < 120:
                status_list.append("LOW PRESSURE")
    return status_list
