import serial

class Listener:
    def __init__(self, com):
        self.ser = serial.Serial(com, "115200", timeout = 1.5)
