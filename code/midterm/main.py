import room_sensor.py

class RoomSensor:
    name = input("이름:")
    temperature = input("온도:")
    humidity = input("습도:")
    light = input("밝기:")
    def__init__(self, roomname):
        self.roomname = roomname
        print(f"방 이름: {self.roomname}")
        
sensor1 = RoomSensor("거실")
sensor2 = RoomSensor("별장")
sensor3 = RoomSensor("주방")

sensor_list = [sensor1, sensor2, sensor3]
print("\n방 리스트:")
for sensor in sensor_list:
    print(f"- {sensor.roomname}")

show_info():
    ("Sensor:" name, "Temperature:" temperature, "Humidity:" humidity, "Light:" light)
comfort_level():
    if (temperature >= 20 and <= 26) and (humidity >= 40 and <= 60):
        "Comfortable"
    elif temperature >= 30 or humidity >= 70:
        "Warning"
    else:
        "Normal"
light_status():
    if light < 200:
        "Dark"
    else:
        "Bright"

for i in RoomSensor:
    print("Sensor:" sensor, "Temperature:" temperature, "Humidity:" humidity, "Light:" light, "Comfort Level:" comfort_level(), "Light Status:" light_status())