import pygame, Support, socketio, subprocess
from pygame import *


handServer = subprocess.Popen('node ./index.js')

xWidth = 800
yHeight = 600
zDepth = 400
handMinimums = (-350, -300, 600)


guiSupport = Support.GUI_Support()
screen = guiSupport.initDisplay((xWidth, yHeight))

def loop(screen, handPos):
    handX, handZ, handY = zeroBounds(handMinimums, handPos)
    guiSupport.drawGraphics((handX, handY, handZ), screen, (xWidth, yHeight))
    guiSupport.displayMetrics(f'X: {handX},Y: {handY},Z: {handZ}', screen)
    pygame.display.update()

#Listen for hand position from socket server
handPosition = (0, 0, 0)
sio = socketio.Client()
@sio.event
def position_update(data):
    global handPosition
    handPosition = tuple(data)
sio.connect('http://localhost:3000')

def zeroBounds(handMinimums, handPosition):
    xMin, yMin, zMin = handMinimums
    xHand, zHand, yHand = handPosition
    
    xHand += -xMin
    yHand += -yMin
    zHand += -zMin
    
    xHand = int(xHand)
    yHand = int(yHand)
    zHand = int(-zHand)

    return (xHand, yHand, zHand)


running = True

while running:
    loop(screen, handPosition)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

pygame.display.quit()
sio.disconnect()
handServer.terminate()