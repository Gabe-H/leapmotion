import serial
import time

class USB_Support:

    def initUSB(self, port, baudrate):
        return serial.Serial(port, baudrate)

    def connect(self, serial):
        serial.write(b"\r\n\r\n")
        time.sleep(2)   # Wait for grbl to initialize
        serial.flushInput()  # Flush startup text in serial input

    def write(self, string, serial):
        string += '\n'
        # serial.write(str.encode(string))
        print(string)
    
    def stop(self, serial):
        serial.close()