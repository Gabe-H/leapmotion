import pygame, math


class GUI_Support:

    def initDisplay(self, dims):
        pygame.init()
        return pygame.display.set_mode(dims)
    
    def drawPosition(self, position, strength, dims, screen):
        handX, handY, handZ = position
        width, height = dims
        pygame.draw.line(screen, (255, 0, 0), (0, handY), (width, handY))
        pygame.draw.line(screen, (0, 255, 0), (handX, 0), (handX, height))

        circleRadius = int(handZ / 20) if (handZ / 20) > 0 else 1
        pygame.draw.circle(screen, (255*strength, 255*strength, 255-(strength*255)), (handX, handY), circleRadius)

    def getTextObjects(self, text, font):
        textSurface = font.render(text, True, (255,255,255))
        return textSurface, textSurface.get_rect()

    def drawText(self, text, y, fontSize, screen):
        largeText = pygame.font.Font('src/Lato-Medium.ttf', fontSize)
        TextSurf, TextRect = self.getTextObjects(text, largeText)
        TextRect.left = 0
        TextRect.top = y
        screen.blit(TextSurf, TextRect)
   
    def displayMetrics(self, data, index, screen):
        fontSize = 25
        data = data.split(',')
        index *= (len(data)+1) * 25
        for i in range(len(data)):
            self.drawText(data[i], i * fontSize + index, fontSize, screen)

    def drawVector(self, data, index, width, screen):
        vecX, vecY, vecZ = data
        vecZ += 0 # Just remove unused variable error lmao
        x = width - 50
        y = index*100 + 50
        pygame.draw.line(screen, (255, 0, 0), (x, y), (x + (50*vecX), y))
        pygame.draw.line(screen, (0, 255, 0), (x, y), (x, y + (50 * -vecY)))

    def updateDisplay(self, screen):
        pygame.display.update()
        screen.fill((0, 0, 0))
    

        