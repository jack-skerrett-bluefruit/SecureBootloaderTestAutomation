import serial
import time

class CommandWriter():
    def __init__(self, com):
        self.ser = serial.Serial(com, "115200", timeout = 1.5)

    def send_command(self, command):
        self.ser.flush()
        final_command = '$' + command + '\r'
        self.ser.write(str.encode(final_command))
        return self.ser.read(len(command))

    
    def check_state(self, command):
        self.ser.flush()
        state = self.send_command(command)
        var = bool(int(state))
        return var