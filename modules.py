def field_status_check(sensor):
    status_list = []
    print("Checking status")
    print(type(sensor))
    for key, value in sensor.items():
        print("for loop")
        if key == "temperature":
            if value > 50:
              
                status_list.append("HIGH TEMPERATURE")
        elif key == "vibration":
            if value >= 6:
                status_list.append("HIGH VIBRATION")
        elif key == "pressure":
            if value < 120:
                status_list.append("LOW PRESSURE")
    print(status_list)
    #return "Status Ok" if len(status_list) == 0 else status_list
