# main.py

from device import SensorDevice, ActuratorDevice, TemperatureSensor, LightSensor

sensor = SensorDevice("Temp Sensor")
actuator = ActualDevice("LED Controller")

sensor.connect()
actuator.connect()

print(sensor.status())
print(actuator.status())
print()

Temp = TemperatureSensor("Temp1")
Light = LightSensor("Light1")

print("Temp: ", temp.read())
print("Light: ", light.read())