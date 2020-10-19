import pygame, Support, socketio, subprocess
from pygame import *


handServer = subprocess.Popen('node ./index.js')

xWidth = 700
yHeight = 600
zDepth = 400
handMinimums = (-350, -300, 200)

guiSupport = Support.GUI_Support()
screen = guiSupport.initDisplay((xWidth, yHeight))

def loop(screen, handPos):
    handX, handZ, handY = handPos
    handX = int(handX+300)
    handY = int(handY+300)
    handZ = int(handZ)
    guiSupport.drawGraphics((handX, handY, handZ), screen, (xWidth, yHeight))
    pygame.display.update()

#Listen for hand position from socket server
handPosition = (0, 0, 0)
sio = socketio.Client()
@sio.event
def position_update(data):
    global handPosition
    handPosition = tuple(data)
sio.connect('http://localhost:3000')

running = True

while running:
    loop(screen, handPosition)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    if guiSupport.isQuit(): break

pygame.display.quit()
sio.disconnect()
handServer.terminate()