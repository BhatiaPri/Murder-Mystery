#******************************
#Authors: Emma Du and Prisha Bhatia
#Date: January 7th, 2022 
#Name: Main menu for the chilling case of Scott Maguire
#Description: This is the main menu for our game that gives access to all other options for the game
#******************************
#importing pygame
import pygame 
import menuButton

pygame.init()

#creating display screen
displayWidth, displayHeight = 800, 600
white = (255, 255, 255)
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Main Menu")

#starting the clock 
clock = pygame.time.Clock()

#loading in button images
menu_exit_img = pygame.image.load('menu_exit.png').convert_alpha()
menu_instructions_img = pygame.image.load('instructions.png').convert_alpha()
menu_quiz_img = pygame.image.load('quiz.png').convert_alpha()
menu_backstory_img = pygame.image.load('backstory.png').convert_alpha()
menu_replay_img = pygame.image.load('replaycutscene.png').convert_alpha()
menu_play_img = pygame.image.load('play.png').convert_alpha()

exitButton = menuButton.Button(525, 350, menu_exit_img, 0.4)
instructionsButton = menuButton.Button(100, 200, menu_instructions_img, 0.4)
quizButton = menuButton.Button(300, 350, menu_quiz_img, 0.4)
backstoryButton = menuButton.Button(100, 350, menu_backstory_img, 0.4)
replayButton = menuButton.Button(500, 185,menu_replay_img, 0.5)
playButton = menuButton.Button(300, 200, menu_play_img, 0.4)

#loading in background image
menuImg = pygame.image.load('menu_bg.png') 
menuImg = pygame.transform.scale(menuImg, (800, 600))

def mainMenu (x, y):
  gameDisplay.blit(menuImg, (x, y))

#Loop
def menuLoop():
  x = (displayWidth * 0.01)
  y = (displayHeight * 0.01)
  gameExit = False

  while gameExit == False:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit() 
    
    gameDisplay.fill(white)
    mainMenu(x, y)

    if exitButton.draw(gameDisplay) == True:
      gameExit = True
    if instructionsButton.draw(gameDisplay) == True:
      print("Instructions") #temporary placeholder
    if quizButton.draw(gameDisplay) == True:
      print("Quiz") #Temporary placeholder
    if backstoryButton.draw(gameDisplay) == True:
      print("Backstory/lesson") #temporary placeholder
    if replayButton.draw(gameDisplay) == True:
      print("Replay Cutscene") #Temporary placeholder
    if playButton.draw(gameDisplay) == True:
      print("Play") #Temporary placeholder

    pygame.display.update()
    clock.tick(60)
menuLoop()   
