import pygame, socketio, subprocess
from pygame import *
from src import Support#, USB

handServer = subprocess.Popen('node node/index.js')

xWidth = 800
yHeight = 600
handMinimums = (-350, -300, 650)

guiSupport = Support.GUI_Support()
screen = guiSupport.initDisplay((xWidth, yHeight))
# serial = USB.USB_Support()

# ser = serial.initUSB('COM5', 115200)
# serial.connect(ser)
# serial.write('G28 X Y', ser)
# serial.write('G0 F10000', ser)
# serial.write('G0 X100 Y0', ser)
# serial.write('G0 X100 Y100', ser)
# serial.write('G0 X0 Y100', ser)
# serial.write('G0 X0 Y0', ser)

def callibratedCoords(pos):
    x, y, z = pos
    x = int((xWidth/2)+x)
    y = int(yHeight-y)
    z = int(z + 500 / 2)

    return (x, y, z)

def loop(screen, data):
    for i in range(len(data)):
        side = data[i]['side']
        pos = data[i]['position']
        handX, handY, handZ = pos
        grip = data[i]['grip']
        guiSupport.displayMetrics(f'{side} hand, X: {handX}, Y: {handY}, Z: {handZ}, G: {grip}', i, screen)
        guiSupport.drawGraphics(callibratedCoords(pos), grip, (xWidth, yHeight), screen)
    guiSupport.updateDisplay(screen)

handData = []
sio = socketio.Client()
@sio.event
def position_update(data):
    global handData
    handData = data
sio.connect('http://localhost:3000')

running = True
while running:
    loop(screen, handData)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

pygame.display.quit()
# serial.stop(ser)
sio.disconnect()
handServer.terminate()