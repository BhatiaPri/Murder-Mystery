#import pygame
import pygame 

pygame.init()

#button class for main menu 
class Button():
  def __init__(self, x, y, image, scale):
    width = image.get_width()
    height = image.get_height()
    self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
    self.rect = self.image.get_rect()
    self.rect.topleft = (x, y)
    self.clicked = False

  def draw(self, surface): 
    action = False
    #get mouse position 
    mousePosition = pygame.mouse.get_pos()

    #check if mouse is on button, and if clicked
    if self.rect.collidepoint(mousePosition):
      if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
        self.clicked = True
        action = True

    if pygame.mouse.get_pressed()[0] == 0:
      self.clicked = False

    #draws button on screen
    surface.blit(self.image, (self.rect.x, self.rect.y))

    return action
