import math
import pygame
from pygame import mixer
from Characters.Characters import Ghost, Monster
from Characters.Position import Position

ScreenResolution =  (600,500)
BackgroundColor = (117,80,123)
initialPosition = {
    'monster': Position((0,0)),
    'ghost': Position((100,10))
}

background = pygame.image.load('./assets/img/background.jpg')

pygame.init()

Points = 0
font1 = pygame.font.Font('freesansbold.ttf',20)
font2 = pygame.font.SysFont('Segoe UI',18)

mixer.music.load('./assets/audio.wav')
mixer.music.play(-1)

def show_texts():
    text1 = font1.render('Puntos: '+str(puntos), True, (255,255,255))
    text2 = font1.render('Python Club de software EPN', True, (255,255,255))
    text3 = font1.render('Cristopher Herrera', True, (255,255,255))
    screen.blit(text1,(25,440))
    screen.blit(text2,(280,430))
    screen.blit(text3,(292,455))

screen = pygame.display.set_mode(ScreenResolution)

ghost = Ghost(initialPosition['ghost'], screen)
monster = Monster(initialPosition['monster'],screen)

moveLeft = False
moveRight = False
moveUp = False
moveDown = False

end = False

while not end:
    screen.fill(BackgroundColor)
    screen.blit(background,(0,0))

    # Game settings
    pygame.display.set_caption("Mounsters")  

    # Dynamic elements

    # Events Manager
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moveLeft = True
            if event.key == pygame.K_RIGHT:
                moveRight = True
            if event.key == pygame.K_UP:
                moveUp = True
            if event.key == pygame.K_DOWN:
                moveDown = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moveLeft = False
            if event.key == pygame.K_RIGHT:
                moveRight = False
            if event.key == pygame.K_UP:
                moveUp = False
            if event.key == pygame.K_DOWN:
                moveDown = False              

    # Make moves
    if moveLeft:
        ghost.position.setX(ghost.position.getCoordinates()[0]-1)
    elif moveRight:
        ghost.position.setX(ghost.position.getCoordinates()[0]+1)
    elif moveUp:
        ghost.position.setY(ghost.position.getCoordinates()[1]-1)
    elif moveDown:
        ghost.position.setY(ghost.position.getCoordinates()[1]+1)

    CharacterCoordinates = ghost.position.getCoordinates()

    # Borders control
    if CharacterCoordinates[0] < 0:
        ghost.position.setX(0)
    elif CharacterCoordinates[0] > 500:
        ghost.posicion.setX(500)
    if CharacterCoordinates[1] < 0:
        ghost.posicion.setY(0)
    elif CharacterCoordinates[1] > 320:
        ghost.posicion.setY(320)

    d = math.sqrt((monster.position.getCoordinates()[0] - ghost.position.getCoordinates()[0])**2+(monster.position.getCoordinates()[1] - ghost.position.getCoordinates()[1])**2)

    print('Distancia: ',d)
    if d < 30:
        scream = mixer.Sound('./assets/grito.wav')
        scream.play()
        Points +=1

    ghost.draw()
    monster.draw()

    pygame.display.update()