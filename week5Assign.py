import random
class Sensor:
    def __init__(self, name: str, location: str): 
        self.name = name
        self.location = location
        self._value = None
    def read_value(self) ->float:
        pass

    def __str__ (self):
        return f"{self.name} at {self.location}: {self._value}"

class TemperatureSensor(Sensor):
    def __init__(self, name: str, location: str, unit="C°"):
        super().__init__(name, location)
        self.unit = unit

    def read_value(self) -> float:
        self._value = round(random.uniform(20.0, 30.0))
        return self._value

    def __str__(self):
        return f"{super().__str__()}{self.unit}"
class HumiditySensor(Sensor):
    def __init__(self, name: str, location: str, unit="%"):
        super().__init__(name, location)
        self.unit = unit

    def read_value(self) -> float:
        self._value = round(random.uniform(40, 60))
        return self._value

    def __str__(self):
        return f"{super().__str__()}{self.unit}"

class CarbonDioxideSensor(Sensor):
    def __init__(self, name: str, location: str, unit="ppm"):
        super().__init__(name, location)
        self.unit = unit

    def read_value(self) -> float:
        self._value = round(random.uniform(10000, 20000))
        return self._value

    def __str__(self):
        return f"{super().__str__()}{self.unit}"

class MotionSensor(Sensor):
    def __init__(self, name: str, location: str):
        super().__init__(name, location)

    def read_value(self) -> bool:
        motion_detected = random.choice([True,False])
        self._value = motion_detected
        return self._value

    def __str__(self):
        return f"{super().__str__()}"

temp_sensor1 = TemperatureSensor("Room Temperature","mushroom far>
temp_sensor1.read_value()
print(temp_sensor1)
hum_sensor1 = HumiditySensor("Internal Humidity","mushroom farm")
hum_sensor1.read_value()
print(hum_sensor1)
co2_sensor = CarbonDioxideSensor("Carbon IV Oxide", "mushroom far>
co2_sensor.read_value()
print(co2_sensor)
motion_sensor = MotionSensor("Motion Detected", "mushroom farm")
motion_sensor.read_value()
print(motion_sensor)
