import serial
import time

ser = serial.Serial('COM5', 115200)

time.sleep(2)

# Wake up grbl
ser.write(b"\r\n\r\n")
time.sleep(2)   # Wait for grbl to initialize
ser.flushInput()  # Flush startup text in serial input
time.sleep(1)
ser.write(b'G28 X Y\n')
ser.write(b'G0 X50 Y50 \n')
time.sleep(1)
ser.close()