import pygame, socketio, subprocess
from pygame import *
from src import Support

handServer = subprocess.Popen('node node/index.js')

xWidth = 800
yHeight = 600
handMinimums = (-350, -300, 650)

guiSupport = Support.GUI_Support()
screen = guiSupport.initDisplay((xWidth, yHeight))

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
sio.disconnect()
handServer.terminate()